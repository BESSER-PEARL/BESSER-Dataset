from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class UseCase_UseCase:

    pass


class Actor_Actor:

    pass





class WIS_HiTierImport:

    def __init__(self, datum: str, benutzer18: "Benutzer" = None, tier21: set["WIS_Tier"] = None):
        self.datum = datum
        self.benutzer18 = benutzer18
        self.tier21 = tier21 if tier21 is not None else set()
        
        pass
    @property
    def datum(self):
        return self.__datum
    @datum.setter
    def datum(self, datum: str):
        self.__datum = datum

    @property
    def tier21(self):
        return self.__tier21
    @tier21.setter
    def tier21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_HiTierImport__tier21", None)
        self.__tier21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hiTierImport20"):
                    opp_val = getattr(item, "hiTierImport20", None)
                    
                    if opp_val == self:
                        setattr(item, "hiTierImport20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hiTierImport20"):
                    opp_val = getattr(item, "hiTierImport20", None)
                    
                    setattr(item, "hiTierImport20", self)
                    

    @property
    def benutzer18(self):
        return self.__benutzer18
    @benutzer18.setter
    def benutzer18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_HiTierImport__benutzer18", None)
        self.__benutzer18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hiTierImport19"):
                opp_val = getattr(old_value, "hiTierImport19", None)
                if opp_val == self:
                    setattr(old_value, "hiTierImport19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hiTierImport19"):
                opp_val = getattr(value, "hiTierImport19", None)
                setattr(value, "hiTierImport19", self)



class WIS_WeideBemerkung:

    def __init__(self, datum: str, bemerkung: str, weideFACTCode: str, weideSchlagnummer: str, weideName: str):
        self.datum = datum
        self.bemerkung = bemerkung
        self.weideFACTCode = weideFACTCode
        self.weideSchlagnummer = weideSchlagnummer
        self.weideName = weideName
        
        pass
    @property
    def weideFACTCode(self):
        return self.__weideFACTCode
    @weideFACTCode.setter
    def weideFACTCode(self, weideFACTCode: str):
        self.__weideFACTCode = weideFACTCode

    @property
    def datum(self):
        return self.__datum
    @datum.setter
    def datum(self, datum: str):
        self.__datum = datum

    @property
    def weideSchlagnummer(self):
        return self.__weideSchlagnummer
    @weideSchlagnummer.setter
    def weideSchlagnummer(self, weideSchlagnummer: str):
        self.__weideSchlagnummer = weideSchlagnummer

    @property
    def weideName(self):
        return self.__weideName
    @weideName.setter
    def weideName(self, weideName: str):
        self.__weideName = weideName

    @property
    def bemerkung(self):
        return self.__bemerkung
    @bemerkung.setter
    def bemerkung(self, bemerkung: str):
        self.__bemerkung = bemerkung



class WIS_Tier:

    def __init__(self, LOM: int, name: str, transponderNummer: str, geburtsdatum: str, istWeiblich: bool, eigeneAngaben: str, letzteKalbung: str, istAktiv: bool, UDNummer: str, BTV4: str, BTV8: str, benutzer0: "Benutzer" = None, herde8: "WIS_Herde" = None, weidegang11: set["WIS_Weidegang"] = None, hiTierImport20: "WIS_HiTierImport" = None):
        self.LOM = LOM
        self.name = name
        self.transponderNummer = transponderNummer
        self.geburtsdatum = geburtsdatum
        self.istWeiblich = istWeiblich
        self.eigeneAngaben = eigeneAngaben
        self.letzteKalbung = letzteKalbung
        self.istAktiv = istAktiv
        self.UDNummer = UDNummer
        self.BTV4 = BTV4
        self.BTV8 = BTV8
        self.benutzer0 = benutzer0
        self.herde8 = herde8
        self.weidegang11 = weidegang11 if weidegang11 is not None else set()
        self.hiTierImport20 = hiTierImport20
        
        pass
    @property
    def UDNummer(self):
        return self.__UDNummer
    @UDNummer.setter
    def UDNummer(self, UDNummer: str):
        self.__UDNummer = UDNummer

    @property
    def transponderNummer(self):
        return self.__transponderNummer
    @transponderNummer.setter
    def transponderNummer(self, transponderNummer: str):
        self.__transponderNummer = transponderNummer

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def istAktiv(self):
        return self.__istAktiv
    @istAktiv.setter
    def istAktiv(self, istAktiv: bool):
        self.__istAktiv = istAktiv

    @property
    def BTV8(self):
        return self.__BTV8
    @BTV8.setter
    def BTV8(self, BTV8: str):
        self.__BTV8 = BTV8

    @property
    def eigeneAngaben(self):
        return self.__eigeneAngaben
    @eigeneAngaben.setter
    def eigeneAngaben(self, eigeneAngaben: str):
        self.__eigeneAngaben = eigeneAngaben

    @property
    def istWeiblich(self):
        return self.__istWeiblich
    @istWeiblich.setter
    def istWeiblich(self, istWeiblich: bool):
        self.__istWeiblich = istWeiblich

    @property
    def LOM(self):
        return self.__LOM
    @LOM.setter
    def LOM(self, LOM: int):
        self.__LOM = LOM

    @property
    def letzteKalbung(self):
        return self.__letzteKalbung
    @letzteKalbung.setter
    def letzteKalbung(self, letzteKalbung: str):
        self.__letzteKalbung = letzteKalbung

    @property
    def BTV4(self):
        return self.__BTV4
    @BTV4.setter
    def BTV4(self, BTV4: str):
        self.__BTV4 = BTV4

    @property
    def geburtsdatum(self):
        return self.__geburtsdatum
    @geburtsdatum.setter
    def geburtsdatum(self, geburtsdatum: str):
        self.__geburtsdatum = geburtsdatum

    @property
    def benutzer0(self):
        return self.__benutzer0
    @benutzer0.setter
    def benutzer0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_Tier__benutzer0", None)
        self.__benutzer0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tier1"):
                opp_val = getattr(old_value, "tier1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tier1"):
                opp_val = getattr(value, "tier1", None)
                if opp_val is None:
                    setattr(value, "tier1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def herde8(self):
        return self.__herde8
    @herde8.setter
    def herde8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_Tier__herde8", None)
        self.__herde8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tier9"):
                opp_val = getattr(old_value, "tier9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tier9"):
                opp_val = getattr(value, "tier9", None)
                if opp_val is None:
                    setattr(value, "tier9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hiTierImport20(self):
        return self.__hiTierImport20
    @hiTierImport20.setter
    def hiTierImport20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_Tier__hiTierImport20", None)
        self.__hiTierImport20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tier21"):
                opp_val = getattr(old_value, "tier21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tier21"):
                opp_val = getattr(value, "tier21", None)
                if opp_val is None:
                    setattr(value, "tier21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def weidegang11(self):
        return self.__weidegang11
    @weidegang11.setter
    def weidegang11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_Tier__weidegang11", None)
        self.__weidegang11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tier10"):
                    opp_val = getattr(item, "tier10", None)
                    
                    if opp_val == self:
                        setattr(item, "tier10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tier10"):
                    opp_val = getattr(item, "tier10", None)
                    
                    setattr(item, "tier10", self)
                    



class WIS_Herde:

    def __init__(self, name: str, weidegang7: set["WIS_Weidegang"] = None, tier9: set["WIS_Tier"] = None, benutzer12: "Benutzer" = None):
        self.name = name
        self.weidegang7 = weidegang7 if weidegang7 is not None else set()
        self.tier9 = tier9 if tier9 is not None else set()
        self.benutzer12 = benutzer12
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def benutzer12(self):
        return self.__benutzer12
    @benutzer12.setter
    def benutzer12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_Herde__benutzer12", None)
        self.__benutzer12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "herde13"):
                opp_val = getattr(old_value, "herde13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "herde13"):
                opp_val = getattr(value, "herde13", None)
                if opp_val is None:
                    setattr(value, "herde13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tier9(self):
        return self.__tier9
    @tier9.setter
    def tier9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_Herde__tier9", None)
        self.__tier9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "herde8"):
                    opp_val = getattr(item, "herde8", None)
                    
                    if opp_val == self:
                        setattr(item, "herde8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "herde8"):
                    opp_val = getattr(item, "herde8", None)
                    
                    setattr(item, "herde8", self)
                    

    @property
    def weidegang7(self):
        return self.__weidegang7
    @weidegang7.setter
    def weidegang7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_Herde__weidegang7", None)
        self.__weidegang7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "herde6"):
                    opp_val = getattr(item, "herde6", None)
                    
                    if opp_val == self:
                        setattr(item, "herde6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "herde6"):
                    opp_val = getattr(item, "herde6", None)
                    
                    setattr(item, "herde6", self)
                    



class WIS_Weidegang:

    def __init__(self, datum: str, herdeName: str, herdeFarbe: str, tierName: str, istAusgefallen: bool, ausfallgrund: str, weideName: str, weideSchlagnummer: str, weideFACTCode: str, tierLOM: str, weide4: "WIS_Weide" = None, herde6: "WIS_Herde" = None, tier10: "WIS_Tier" = None, benutzer14: "Benutzer" = None):
        self.datum = datum
        self.herdeName = herdeName
        self.herdeFarbe = herdeFarbe
        self.tierName = tierName
        self.istAusgefallen = istAusgefallen
        self.ausfallgrund = ausfallgrund
        self.weideName = weideName
        self.weideSchlagnummer = weideSchlagnummer
        self.weideFACTCode = weideFACTCode
        self.tierLOM = tierLOM
        self.weide4 = weide4
        self.herde6 = herde6
        self.tier10 = tier10
        self.benutzer14 = benutzer14
        
        pass
    @property
    def herdeFarbe(self):
        return self.__herdeFarbe
    @herdeFarbe.setter
    def herdeFarbe(self, herdeFarbe: str):
        self.__herdeFarbe = herdeFarbe

    @property
    def istAusgefallen(self):
        return self.__istAusgefallen
    @istAusgefallen.setter
    def istAusgefallen(self, istAusgefallen: bool):
        self.__istAusgefallen = istAusgefallen

    @property
    def weideFACTCode(self):
        return self.__weideFACTCode
    @weideFACTCode.setter
    def weideFACTCode(self, weideFACTCode: str):
        self.__weideFACTCode = weideFACTCode

    @property
    def datum(self):
        return self.__datum
    @datum.setter
    def datum(self, datum: str):
        self.__datum = datum

    @property
    def tierLOM(self):
        return self.__tierLOM
    @tierLOM.setter
    def tierLOM(self, tierLOM: str):
        self.__tierLOM = tierLOM

    @property
    def weideSchlagnummer(self):
        return self.__weideSchlagnummer
    @weideSchlagnummer.setter
    def weideSchlagnummer(self, weideSchlagnummer: str):
        self.__weideSchlagnummer = weideSchlagnummer

    @property
    def ausfallgrund(self):
        return self.__ausfallgrund
    @ausfallgrund.setter
    def ausfallgrund(self, ausfallgrund: str):
        self.__ausfallgrund = ausfallgrund

    @property
    def herdeName(self):
        return self.__herdeName
    @herdeName.setter
    def herdeName(self, herdeName: str):
        self.__herdeName = herdeName

    @property
    def tierName(self):
        return self.__tierName
    @tierName.setter
    def tierName(self, tierName: str):
        self.__tierName = tierName

    @property
    def weideName(self):
        return self.__weideName
    @weideName.setter
    def weideName(self, weideName: str):
        self.__weideName = weideName

    @property
    def herde6(self):
        return self.__herde6
    @herde6.setter
    def herde6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_Weidegang__herde6", None)
        self.__herde6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "weidegang7"):
                opp_val = getattr(old_value, "weidegang7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "weidegang7"):
                opp_val = getattr(value, "weidegang7", None)
                if opp_val is None:
                    setattr(value, "weidegang7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tier10(self):
        return self.__tier10
    @tier10.setter
    def tier10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_Weidegang__tier10", None)
        self.__tier10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "weidegang11"):
                opp_val = getattr(old_value, "weidegang11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "weidegang11"):
                opp_val = getattr(value, "weidegang11", None)
                if opp_val is None:
                    setattr(value, "weidegang11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def benutzer14(self):
        return self.__benutzer14
    @benutzer14.setter
    def benutzer14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_Weidegang__benutzer14", None)
        self.__benutzer14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "weidegang15"):
                opp_val = getattr(old_value, "weidegang15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "weidegang15"):
                opp_val = getattr(value, "weidegang15", None)
                if opp_val is None:
                    setattr(value, "weidegang15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def weide4(self):
        return self.__weide4
    @weide4.setter
    def weide4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_Weidegang__weide4", None)
        self.__weide4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "weidegang5"):
                opp_val = getattr(old_value, "weidegang5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "weidegang5"):
                opp_val = getattr(value, "weidegang5", None)
                if opp_val is None:
                    setattr(value, "weidegang5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class WIS_Weide:

    def __init__(self, FACTCode: int, farbe: str, istBetriebsfremdeFlaeche: bool, LPRVertrag: str, istAktiv: bool, bemerkung: str, name: str, schlagnummer: int, groesse: int, teilflaeche2: set["WIS_Weidefl_che"] = None, weidegang5: set["WIS_Weidegang"] = None, benutzer16: "Benutzer" = None):
        self.FACTCode = FACTCode
        self.farbe = farbe
        self.istBetriebsfremdeFlaeche = istBetriebsfremdeFlaeche
        self.LPRVertrag = LPRVertrag
        self.istAktiv = istAktiv
        self.bemerkung = bemerkung
        self.name = name
        self.schlagnummer = schlagnummer
        self.groesse = groesse
        self.teilflaeche2 = teilflaeche2 if teilflaeche2 is not None else set()
        self.weidegang5 = weidegang5 if weidegang5 is not None else set()
        self.benutzer16 = benutzer16
        
        pass
    @property
    def schlagnummer(self):
        return self.__schlagnummer
    @schlagnummer.setter
    def schlagnummer(self, schlagnummer: int):
        self.__schlagnummer = schlagnummer

    @property
    def LPRVertrag(self):
        return self.__LPRVertrag
    @LPRVertrag.setter
    def LPRVertrag(self, LPRVertrag: str):
        self.__LPRVertrag = LPRVertrag

    @property
    def bemerkung(self):
        return self.__bemerkung
    @bemerkung.setter
    def bemerkung(self, bemerkung: str):
        self.__bemerkung = bemerkung

    @property
    def istAktiv(self):
        return self.__istAktiv
    @istAktiv.setter
    def istAktiv(self, istAktiv: bool):
        self.__istAktiv = istAktiv

    @property
    def FACTCode(self):
        return self.__FACTCode
    @FACTCode.setter
    def FACTCode(self, FACTCode: int):
        self.__FACTCode = FACTCode

    @property
    def farbe(self):
        return self.__farbe
    @farbe.setter
    def farbe(self, farbe: str):
        self.__farbe = farbe

    @property
    def groesse(self):
        return self.__groesse
    @groesse.setter
    def groesse(self, groesse: int):
        self.__groesse = groesse

    @property
    def istBetriebsfremdeFlaeche(self):
        return self.__istBetriebsfremdeFlaeche
    @istBetriebsfremdeFlaeche.setter
    def istBetriebsfremdeFlaeche(self, istBetriebsfremdeFlaeche: bool):
        self.__istBetriebsfremdeFlaeche = istBetriebsfremdeFlaeche

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def teilflaeche2(self):
        return self.__teilflaeche2
    @teilflaeche2.setter
    def teilflaeche2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_Weide__teilflaeche2", None)
        self.__teilflaeche2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "weide3"):
                    opp_val = getattr(item, "weide3", None)
                    
                    if opp_val == self:
                        setattr(item, "weide3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "weide3"):
                    opp_val = getattr(item, "weide3", None)
                    
                    setattr(item, "weide3", self)
                    

    @property
    def benutzer16(self):
        return self.__benutzer16
    @benutzer16.setter
    def benutzer16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_Weide__benutzer16", None)
        self.__benutzer16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "weide17"):
                opp_val = getattr(old_value, "weide17", None)
                if opp_val == self:
                    setattr(old_value, "weide17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "weide17"):
                opp_val = getattr(value, "weide17", None)
                setattr(value, "weide17", self)

    @property
    def weidegang5(self):
        return self.__weidegang5
    @weidegang5.setter
    def weidegang5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_Weide__weidegang5", None)
        self.__weidegang5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "weide4"):
                    opp_val = getattr(item, "weide4", None)
                    
                    if opp_val == self:
                        setattr(item, "weide4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "weide4"):
                    opp_val = getattr(item, "weide4", None)
                    
                    setattr(item, "weide4", self)
                    



class WIS_Weidefl_che:

    def __init__(self, groesse: int, farbe: str, name: str, schlagnummer: str, weide3: "WIS_Weide" = None):
        self.groesse = groesse
        self.farbe = farbe
        self.name = name
        self.schlagnummer = schlagnummer
        self.weide3 = weide3
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def schlagnummer(self):
        return self.__schlagnummer
    @schlagnummer.setter
    def schlagnummer(self, schlagnummer: str):
        self.__schlagnummer = schlagnummer

    @property
    def groesse(self):
        return self.__groesse
    @groesse.setter
    def groesse(self, groesse: int):
        self.__groesse = groesse

    @property
    def farbe(self):
        return self.__farbe
    @farbe.setter
    def farbe(self, farbe: str):
        self.__farbe = farbe

    @property
    def weide3(self):
        return self.__weide3
    @weide3.setter
    def weide3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WIS_Weidefl_che__weide3", None)
        self.__weide3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teilflaeche2"):
                opp_val = getattr(old_value, "teilflaeche2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teilflaeche2"):
                opp_val = getattr(value, "teilflaeche2", None)
                if opp_val is None:
                    setattr(value, "teilflaeche2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Weidegang2:

    def __init__(self, datum: str, herdeName: str, herdeFarbe: str, tierName: str, istAusgefallen: bool, ausfallgrund: str, weideName: str, weideSchlagnummer: str, weideFACTCode: str):
        self.datum = datum
        self.herdeName = herdeName
        self.herdeFarbe = herdeFarbe
        self.tierName = tierName
        self.istAusgefallen = istAusgefallen
        self.ausfallgrund = ausfallgrund
        self.weideName = weideName
        self.weideSchlagnummer = weideSchlagnummer
        self.weideFACTCode = weideFACTCode
        
        pass
    @property
    def datum(self):
        return self.__datum
    @datum.setter
    def datum(self, datum: str):
        self.__datum = datum

    @property
    def tierName(self):
        return self.__tierName
    @tierName.setter
    def tierName(self, tierName: str):
        self.__tierName = tierName

    @property
    def weideFACTCode(self):
        return self.__weideFACTCode
    @weideFACTCode.setter
    def weideFACTCode(self, weideFACTCode: str):
        self.__weideFACTCode = weideFACTCode

    @property
    def weideSchlagnummer(self):
        return self.__weideSchlagnummer
    @weideSchlagnummer.setter
    def weideSchlagnummer(self, weideSchlagnummer: str):
        self.__weideSchlagnummer = weideSchlagnummer

    @property
    def herdeName(self):
        return self.__herdeName
    @herdeName.setter
    def herdeName(self, herdeName: str):
        self.__herdeName = herdeName

    @property
    def weideName(self):
        return self.__weideName
    @weideName.setter
    def weideName(self, weideName: str):
        self.__weideName = weideName

    @property
    def istAusgefallen(self):
        return self.__istAusgefallen
    @istAusgefallen.setter
    def istAusgefallen(self, istAusgefallen: bool):
        self.__istAusgefallen = istAusgefallen

    @property
    def herdeFarbe(self):
        return self.__herdeFarbe
    @herdeFarbe.setter
    def herdeFarbe(self, herdeFarbe: str):
        self.__herdeFarbe = herdeFarbe

    @property
    def ausfallgrund(self):
        return self.__ausfallgrund
    @ausfallgrund.setter
    def ausfallgrund(self, ausfallgrund: str):
        self.__ausfallgrund = ausfallgrund



class Benutzer:

    def __init__(self, name: str, passwortHash: str, tier1: set["WIS_Tier"] = None, herde13: set["WIS_Herde"] = None, weidegang15: set["WIS_Weidegang"] = None, weide17: "WIS_Weide" = None, hiTierImport19: "WIS_HiTierImport" = None):
        self.name = name
        self.passwortHash = passwortHash
        self.tier1 = tier1 if tier1 is not None else set()
        self.herde13 = herde13 if herde13 is not None else set()
        self.weidegang15 = weidegang15 if weidegang15 is not None else set()
        self.weide17 = weide17
        self.hiTierImport19 = hiTierImport19
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def passwortHash(self):
        return self.__passwortHash
    @passwortHash.setter
    def passwortHash(self, passwortHash: str):
        self.__passwortHash = passwortHash

    @property
    def weide17(self):
        return self.__weide17
    @weide17.setter
    def weide17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Benutzer__weide17", None)
        self.__weide17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "benutzer16"):
                opp_val = getattr(old_value, "benutzer16", None)
                if opp_val == self:
                    setattr(old_value, "benutzer16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "benutzer16"):
                opp_val = getattr(value, "benutzer16", None)
                setattr(value, "benutzer16", self)

    @property
    def tier1(self):
        return self.__tier1
    @tier1.setter
    def tier1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Benutzer__tier1", None)
        self.__tier1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "benutzer0"):
                    opp_val = getattr(item, "benutzer0", None)
                    
                    if opp_val == self:
                        setattr(item, "benutzer0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "benutzer0"):
                    opp_val = getattr(item, "benutzer0", None)
                    
                    setattr(item, "benutzer0", self)
                    

    @property
    def hiTierImport19(self):
        return self.__hiTierImport19
    @hiTierImport19.setter
    def hiTierImport19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Benutzer__hiTierImport19", None)
        self.__hiTierImport19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "benutzer18"):
                opp_val = getattr(old_value, "benutzer18", None)
                if opp_val == self:
                    setattr(old_value, "benutzer18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "benutzer18"):
                opp_val = getattr(value, "benutzer18", None)
                setattr(value, "benutzer18", self)

    @property
    def herde13(self):
        return self.__herde13
    @herde13.setter
    def herde13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Benutzer__herde13", None)
        self.__herde13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "benutzer12"):
                    opp_val = getattr(item, "benutzer12", None)
                    
                    if opp_val == self:
                        setattr(item, "benutzer12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "benutzer12"):
                    opp_val = getattr(item, "benutzer12", None)
                    
                    setattr(item, "benutzer12", self)
                    

    @property
    def weidegang15(self):
        return self.__weidegang15
    @weidegang15.setter
    def weidegang15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Benutzer__weidegang15", None)
        self.__weidegang15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "benutzer14"):
                    opp_val = getattr(item, "benutzer14", None)
                    
                    if opp_val == self:
                        setattr(item, "benutzer14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "benutzer14"):
                    opp_val = getattr(item, "benutzer14", None)
                    
                    setattr(item, "benutzer14", self)
                    

