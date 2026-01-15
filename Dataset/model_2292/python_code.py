from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class zlvp_LegendaTyp:

    def __init__(self, name: str, id: int, zlvp_LegendaTyp: "zlvp_Legenda" = None):
        self.name = name
        self.id = id
        self.zlvp_LegendaTyp = zlvp_LegendaTyp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def zlvp_LegendaTyp(self):
        return self.__zlvp_LegendaTyp

    @zlvp_LegendaTyp.setter
    def zlvp_LegendaTyp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_LegendaTyp__zlvp_LegendaTyp", None)
        self.__zlvp_LegendaTyp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Legenda57"):
                opp_val = getattr(old_value, "zlvp_Legenda57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Legenda57"):
                opp_val = getattr(value, "zlvp_Legenda57", None)
                if opp_val is None:
                    setattr(value, "zlvp_Legenda57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class zlvp_Legenda:

    def __init__(self, id: int, nachname: str, vorname: str, strasse: str, plz: str, handyNr: str, faxNr: str, email: str, firma: str, bemerkung: str, ort: str, telNr: str, zlvp_Legenda: "zlvp_Anrede" = None, zlvp_Legenda57: set["zlvp_LegendaTyp"] = None, zlvp_Legenda60: "zlvp_Lagerort" = None):
        self.id = id
        self.nachname = nachname
        self.vorname = vorname
        self.strasse = strasse
        self.plz = plz
        self.handyNr = handyNr
        self.faxNr = faxNr
        self.email = email
        self.firma = firma
        self.bemerkung = bemerkung
        self.ort = ort
        self.telNr = telNr
        self.zlvp_Legenda = zlvp_Legenda
        self.zlvp_Legenda57 = zlvp_Legenda57 if zlvp_Legenda57 is not None else set()
        self.zlvp_Legenda60 = zlvp_Legenda60
        
    @property
    def handyNr(self) -> str:
        return self.__handyNr

    @handyNr.setter
    def handyNr(self, handyNr: str):
        self.__handyNr = handyNr

    @property
    def strasse(self) -> str:
        return self.__strasse

    @strasse.setter
    def strasse(self, strasse: str):
        self.__strasse = strasse

    @property
    def bemerkung(self) -> str:
        return self.__bemerkung

    @bemerkung.setter
    def bemerkung(self, bemerkung: str):
        self.__bemerkung = bemerkung

    @property
    def telNr(self) -> str:
        return self.__telNr

    @telNr.setter
    def telNr(self, telNr: str):
        self.__telNr = telNr

    @property
    def nachname(self) -> str:
        return self.__nachname

    @nachname.setter
    def nachname(self, nachname: str):
        self.__nachname = nachname

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def vorname(self) -> str:
        return self.__vorname

    @vorname.setter
    def vorname(self, vorname: str):
        self.__vorname = vorname

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def ort(self) -> str:
        return self.__ort

    @ort.setter
    def ort(self, ort: str):
        self.__ort = ort

    @property
    def faxNr(self) -> str:
        return self.__faxNr

    @faxNr.setter
    def faxNr(self, faxNr: str):
        self.__faxNr = faxNr

    @property
    def plz(self) -> str:
        return self.__plz

    @plz.setter
    def plz(self, plz: str):
        self.__plz = plz

    @property
    def firma(self) -> str:
        return self.__firma

    @firma.setter
    def firma(self, firma: str):
        self.__firma = firma

    @property
    def zlvp_Legenda60(self):
        return self.__zlvp_Legenda60

    @zlvp_Legenda60.setter
    def zlvp_Legenda60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Legenda__zlvp_Legenda60", None)
        self.__zlvp_Legenda60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Lagerort59"):
                opp_val = getattr(old_value, "zlvp_Lagerort59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Lagerort59"):
                opp_val = getattr(value, "zlvp_Lagerort59", None)
                if opp_val is None:
                    setattr(value, "zlvp_Lagerort59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def zlvp_Legenda57(self):
        return self.__zlvp_Legenda57

    @zlvp_Legenda57.setter
    def zlvp_Legenda57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Legenda__zlvp_Legenda57", None)
        self.__zlvp_Legenda57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_LegendaTyp"):
                    opp_val = getattr(item, "zlvp_LegendaTyp", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_LegendaTyp", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_LegendaTyp"):
                    opp_val = getattr(item, "zlvp_LegendaTyp", None)
                    
                    setattr(item, "zlvp_LegendaTyp", self)
                    

    @property
    def zlvp_Legenda(self):
        return self.__zlvp_Legenda

    @zlvp_Legenda.setter
    def zlvp_Legenda(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Legenda__zlvp_Legenda", None)
        self.__zlvp_Legenda = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Anrede55"):
                opp_val = getattr(old_value, "zlvp_Anrede55", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Anrede55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Anrede55"):
                opp_val = getattr(value, "zlvp_Anrede55", None)
                setattr(value, "zlvp_Anrede55", self)

class zlvp_ZeltDetailBezeichnung:

    def __init__(self, name: str, id: int, zlvp_ZeltDetailBezeichnung: "zlvp_ZeltDetail" = None):
        self.name = name
        self.id = id
        self.zlvp_ZeltDetailBezeichnung = zlvp_ZeltDetailBezeichnung
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def zlvp_ZeltDetailBezeichnung(self):
        return self.__zlvp_ZeltDetailBezeichnung

    @zlvp_ZeltDetailBezeichnung.setter
    def zlvp_ZeltDetailBezeichnung(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_ZeltDetailBezeichnung__zlvp_ZeltDetailBezeichnung", None)
        self.__zlvp_ZeltDetailBezeichnung = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_ZeltDetail53"):
                opp_val = getattr(old_value, "zlvp_ZeltDetail53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_ZeltDetail53"):
                opp_val = getattr(value, "zlvp_ZeltDetail53", None)
                if opp_val is None:
                    setattr(value, "zlvp_ZeltDetail53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class zlvp_Verleih:

    def __init__(self, id: int, datum: date, person: str, bemerkung: str, zlvp_Verleih: "zlvp_Zelt" = None):
        self.id = id
        self.datum = datum
        self.person = person
        self.bemerkung = bemerkung
        self.zlvp_Verleih = zlvp_Verleih
        
    @property
    def bemerkung(self) -> str:
        return self.__bemerkung

    @bemerkung.setter
    def bemerkung(self, bemerkung: str):
        self.__bemerkung = bemerkung

    @property
    def datum(self) -> date:
        return self.__datum

    @datum.setter
    def datum(self, datum: date):
        self.__datum = datum

    @property
    def person(self) -> str:
        return self.__person

    @person.setter
    def person(self, person: str):
        self.__person = person

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def zlvp_Verleih(self):
        return self.__zlvp_Verleih

    @zlvp_Verleih.setter
    def zlvp_Verleih(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Verleih__zlvp_Verleih", None)
        self.__zlvp_Verleih = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Zelt48"):
                opp_val = getattr(old_value, "zlvp_Zelt48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Zelt48"):
                opp_val = getattr(value, "zlvp_Zelt48", None)
                if opp_val is None:
                    setattr(value, "zlvp_Zelt48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class zlvp_Schaeden:

    def __init__(self, id: int, datum: date, bezeichnung: str, zlvp_Schaeden: "zlvp_Zelt" = None):
        self.id = id
        self.datum = datum
        self.bezeichnung = bezeichnung
        self.zlvp_Schaeden = zlvp_Schaeden
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def bezeichnung(self) -> str:
        return self.__bezeichnung

    @bezeichnung.setter
    def bezeichnung(self, bezeichnung: str):
        self.__bezeichnung = bezeichnung

    @property
    def datum(self) -> date:
        return self.__datum

    @datum.setter
    def datum(self, datum: date):
        self.__datum = datum

    @property
    def zlvp_Schaeden(self):
        return self.__zlvp_Schaeden

    @zlvp_Schaeden.setter
    def zlvp_Schaeden(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Schaeden__zlvp_Schaeden", None)
        self.__zlvp_Schaeden = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Zelt46"):
                opp_val = getattr(old_value, "zlvp_Zelt46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Zelt46"):
                opp_val = getattr(value, "zlvp_Zelt46", None)
                if opp_val is None:
                    setattr(value, "zlvp_Zelt46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class zlvp_ZeltDetail:

    def __init__(self, id: int, name: str, zlvp_ZeltDetail: "zlvp_Zelt" = None, zlvp_ZeltDetail53: set["zlvp_ZeltDetailBezeichnung"] = None):
        self.id = id
        self.name = name
        self.zlvp_ZeltDetail = zlvp_ZeltDetail
        self.zlvp_ZeltDetail53 = zlvp_ZeltDetail53 if zlvp_ZeltDetail53 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def zlvp_ZeltDetail(self):
        return self.__zlvp_ZeltDetail

    @zlvp_ZeltDetail.setter
    def zlvp_ZeltDetail(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_ZeltDetail__zlvp_ZeltDetail", None)
        self.__zlvp_ZeltDetail = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Zelt44"):
                opp_val = getattr(old_value, "zlvp_Zelt44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Zelt44"):
                opp_val = getattr(value, "zlvp_Zelt44", None)
                if opp_val is None:
                    setattr(value, "zlvp_Zelt44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def zlvp_ZeltDetail53(self):
        return self.__zlvp_ZeltDetail53

    @zlvp_ZeltDetail53.setter
    def zlvp_ZeltDetail53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_ZeltDetail__zlvp_ZeltDetail53", None)
        self.__zlvp_ZeltDetail53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_ZeltDetailBezeichnung"):
                    opp_val = getattr(item, "zlvp_ZeltDetailBezeichnung", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_ZeltDetailBezeichnung", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_ZeltDetailBezeichnung"):
                    opp_val = getattr(item, "zlvp_ZeltDetailBezeichnung", None)
                    
                    setattr(item, "zlvp_ZeltDetailBezeichnung", self)
                    

class zlvp_Zelt:

    def __init__(self, id: int, name: str, zlvp_Zelt: "zlvp_Lager" = None, zlvp_Zelt44: set["zlvp_ZeltDetail"] = None, zlvp_Zelt46: set["zlvp_Schaeden"] = None, zlvp_Zelt48: set["zlvp_Verleih"] = None, zlvp_Zelt50: set["zlvp_Lager"] = None):
        self.id = id
        self.name = name
        self.zlvp_Zelt = zlvp_Zelt
        self.zlvp_Zelt44 = zlvp_Zelt44 if zlvp_Zelt44 is not None else set()
        self.zlvp_Zelt46 = zlvp_Zelt46 if zlvp_Zelt46 is not None else set()
        self.zlvp_Zelt48 = zlvp_Zelt48 if zlvp_Zelt48 is not None else set()
        self.zlvp_Zelt50 = zlvp_Zelt50 if zlvp_Zelt50 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def zlvp_Zelt(self):
        return self.__zlvp_Zelt

    @zlvp_Zelt.setter
    def zlvp_Zelt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Zelt__zlvp_Zelt", None)
        self.__zlvp_Zelt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Lager31"):
                opp_val = getattr(old_value, "zlvp_Lager31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Lager31"):
                opp_val = getattr(value, "zlvp_Lager31", None)
                if opp_val is None:
                    setattr(value, "zlvp_Lager31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def zlvp_Zelt44(self):
        return self.__zlvp_Zelt44

    @zlvp_Zelt44.setter
    def zlvp_Zelt44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Zelt__zlvp_Zelt44", None)
        self.__zlvp_Zelt44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_ZeltDetail"):
                    opp_val = getattr(item, "zlvp_ZeltDetail", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_ZeltDetail", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_ZeltDetail"):
                    opp_val = getattr(item, "zlvp_ZeltDetail", None)
                    
                    setattr(item, "zlvp_ZeltDetail", self)
                    

    @property
    def zlvp_Zelt50(self):
        return self.__zlvp_Zelt50

    @zlvp_Zelt50.setter
    def zlvp_Zelt50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Zelt__zlvp_Zelt50", None)
        self.__zlvp_Zelt50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Lager51"):
                    opp_val = getattr(item, "zlvp_Lager51", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Lager51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Lager51"):
                    opp_val = getattr(item, "zlvp_Lager51", None)
                    
                    setattr(item, "zlvp_Lager51", self)
                    

    @property
    def zlvp_Zelt48(self):
        return self.__zlvp_Zelt48

    @zlvp_Zelt48.setter
    def zlvp_Zelt48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Zelt__zlvp_Zelt48", None)
        self.__zlvp_Zelt48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Verleih"):
                    opp_val = getattr(item, "zlvp_Verleih", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Verleih", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Verleih"):
                    opp_val = getattr(item, "zlvp_Verleih", None)
                    
                    setattr(item, "zlvp_Verleih", self)
                    

    @property
    def zlvp_Zelt46(self):
        return self.__zlvp_Zelt46

    @zlvp_Zelt46.setter
    def zlvp_Zelt46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Zelt__zlvp_Zelt46", None)
        self.__zlvp_Zelt46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Schaeden"):
                    opp_val = getattr(item, "zlvp_Schaeden", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Schaeden", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Schaeden"):
                    opp_val = getattr(item, "zlvp_Schaeden", None)
                    
                    setattr(item, "zlvp_Schaeden", self)
                    

class zlvp_Lagerort:

    def __init__(self, id: int, name: str, zlvp_Lagerort: "zlvp_Lager" = None, zlvp_Lagerort59: set["zlvp_Legenda"] = None, zlvp_Lagerort62: set["zlvp_Lager"] = None):
        self.id = id
        self.name = name
        self.zlvp_Lagerort = zlvp_Lagerort
        self.zlvp_Lagerort59 = zlvp_Lagerort59 if zlvp_Lagerort59 is not None else set()
        self.zlvp_Lagerort62 = zlvp_Lagerort62 if zlvp_Lagerort62 is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def zlvp_Lagerort62(self):
        return self.__zlvp_Lagerort62

    @zlvp_Lagerort62.setter
    def zlvp_Lagerort62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Lagerort__zlvp_Lagerort62", None)
        self.__zlvp_Lagerort62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Lager63"):
                    opp_val = getattr(item, "zlvp_Lager63", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Lager63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Lager63"):
                    opp_val = getattr(item, "zlvp_Lager63", None)
                    
                    setattr(item, "zlvp_Lager63", self)
                    

    @property
    def zlvp_Lagerort(self):
        return self.__zlvp_Lagerort

    @zlvp_Lagerort.setter
    def zlvp_Lagerort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Lagerort__zlvp_Lagerort", None)
        self.__zlvp_Lagerort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Lager36"):
                opp_val = getattr(old_value, "zlvp_Lager36", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Lager36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Lager36"):
                opp_val = getattr(value, "zlvp_Lager36", None)
                setattr(value, "zlvp_Lager36", self)

    @property
    def zlvp_Lagerort59(self):
        return self.__zlvp_Lagerort59

    @zlvp_Lagerort59.setter
    def zlvp_Lagerort59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Lagerort__zlvp_Lagerort59", None)
        self.__zlvp_Lagerort59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Legenda60"):
                    opp_val = getattr(item, "zlvp_Legenda60", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Legenda60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Legenda60"):
                    opp_val = getattr(item, "zlvp_Legenda60", None)
                    
                    setattr(item, "zlvp_Legenda60", self)
                    

class zlvp_Programm:

    def __init__(self, id: int, datum: date, vormittag: str, nachmittag: str, nacht: str, zlvp_Programm: "zlvp_Lager" = None):
        self.id = id
        self.datum = datum
        self.vormittag = vormittag
        self.nachmittag = nachmittag
        self.nacht = nacht
        self.zlvp_Programm = zlvp_Programm
        
    @property
    def nachmittag(self) -> str:
        return self.__nachmittag

    @nachmittag.setter
    def nachmittag(self, nachmittag: str):
        self.__nachmittag = nachmittag

    @property
    def datum(self) -> date:
        return self.__datum

    @datum.setter
    def datum(self, datum: date):
        self.__datum = datum

    @property
    def nacht(self) -> str:
        return self.__nacht

    @nacht.setter
    def nacht(self, nacht: str):
        self.__nacht = nacht

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def vormittag(self) -> str:
        return self.__vormittag

    @vormittag.setter
    def vormittag(self, vormittag: str):
        self.__vormittag = vormittag

    @property
    def zlvp_Programm(self):
        return self.__zlvp_Programm

    @zlvp_Programm.setter
    def zlvp_Programm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Programm__zlvp_Programm", None)
        self.__zlvp_Programm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Lager29"):
                opp_val = getattr(old_value, "zlvp_Lager29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Lager29"):
                opp_val = getattr(value, "zlvp_Lager29", None)
                if opp_val is None:
                    setattr(value, "zlvp_Lager29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class zlvp_Essen:

    def __init__(self, vormittag: str, nachmittag: str, nacht: str, id: int, datum: date, zlvp_Essen: "zlvp_Lager" = None):
        self.vormittag = vormittag
        self.nachmittag = nachmittag
        self.nacht = nacht
        self.id = id
        self.datum = datum
        self.zlvp_Essen = zlvp_Essen
        
    @property
    def datum(self) -> date:
        return self.__datum

    @datum.setter
    def datum(self, datum: date):
        self.__datum = datum

    @property
    def nachmittag(self) -> str:
        return self.__nachmittag

    @nachmittag.setter
    def nachmittag(self, nachmittag: str):
        self.__nachmittag = nachmittag

    @property
    def nacht(self) -> str:
        return self.__nacht

    @nacht.setter
    def nacht(self, nacht: str):
        self.__nacht = nacht

    @property
    def vormittag(self) -> str:
        return self.__vormittag

    @vormittag.setter
    def vormittag(self, vormittag: str):
        self.__vormittag = vormittag

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def zlvp_Essen(self):
        return self.__zlvp_Essen

    @zlvp_Essen.setter
    def zlvp_Essen(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Essen__zlvp_Essen", None)
        self.__zlvp_Essen = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Lager27"):
                opp_val = getattr(old_value, "zlvp_Lager27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Lager27"):
                opp_val = getattr(value, "zlvp_Lager27", None)
                if opp_val is None:
                    setattr(value, "zlvp_Lager27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class zlvp_Jahr:

    def __init__(self, id: int, name: str, zlvp_Jahr: set["zlvp_Lager"] = None):
        self.id = id
        self.name = name
        self.zlvp_Jahr = zlvp_Jahr if zlvp_Jahr is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def zlvp_Jahr(self):
        return self.__zlvp_Jahr

    @zlvp_Jahr.setter
    def zlvp_Jahr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Jahr__zlvp_Jahr", None)
        self.__zlvp_Jahr = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Lager19"):
                    opp_val = getattr(item, "zlvp_Lager19", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Lager19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Lager19"):
                    opp_val = getattr(item, "zlvp_Lager19", None)
                    
                    setattr(item, "zlvp_Lager19", self)
                    

class zlvp_Lager:

    def __init__(self, id: int, name: str, start: date, stop: date, thema: str, ort: str, zlvp_Lager: "zlvp_Stab" = None, zlvp_Lager19: "zlvp_Jahr" = None, zlvp_Lager21: set["zlvp_Gruppen"] = None, zlvp_Lager24: set["zlvp_Stab"] = None, zlvp_Lager27: set["zlvp_Essen"] = None, zlvp_Lager29: set["zlvp_Programm"] = None, zlvp_Lager33: set["zlvp_Person"] = None, zlvp_Lager36: "zlvp_Lagerort" = None, zlvp_Lager31: set["zlvp_Zelt"] = None, zlvp_Lager51: "zlvp_Zelt" = None, zlvp_Lager63: "zlvp_Lagerort" = None):
        self.id = id
        self.name = name
        self.start = start
        self.stop = stop
        self.thema = thema
        self.ort = ort
        self.zlvp_Lager = zlvp_Lager
        self.zlvp_Lager19 = zlvp_Lager19
        self.zlvp_Lager21 = zlvp_Lager21 if zlvp_Lager21 is not None else set()
        self.zlvp_Lager24 = zlvp_Lager24 if zlvp_Lager24 is not None else set()
        self.zlvp_Lager27 = zlvp_Lager27 if zlvp_Lager27 is not None else set()
        self.zlvp_Lager29 = zlvp_Lager29 if zlvp_Lager29 is not None else set()
        self.zlvp_Lager33 = zlvp_Lager33 if zlvp_Lager33 is not None else set()
        self.zlvp_Lager36 = zlvp_Lager36
        self.zlvp_Lager31 = zlvp_Lager31 if zlvp_Lager31 is not None else set()
        self.zlvp_Lager51 = zlvp_Lager51
        self.zlvp_Lager63 = zlvp_Lager63
        
    @property
    def ort(self) -> str:
        return self.__ort

    @ort.setter
    def ort(self, ort: str):
        self.__ort = ort

    @property
    def stop(self) -> date:
        return self.__stop

    @stop.setter
    def stop(self, stop: date):
        self.__stop = stop

    @property
    def thema(self) -> str:
        return self.__thema

    @thema.setter
    def thema(self, thema: str):
        self.__thema = thema

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def start(self) -> date:
        return self.__start

    @start.setter
    def start(self, start: date):
        self.__start = start

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def zlvp_Lager29(self):
        return self.__zlvp_Lager29

    @zlvp_Lager29.setter
    def zlvp_Lager29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Lager__zlvp_Lager29", None)
        self.__zlvp_Lager29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Programm"):
                    opp_val = getattr(item, "zlvp_Programm", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Programm", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Programm"):
                    opp_val = getattr(item, "zlvp_Programm", None)
                    
                    setattr(item, "zlvp_Programm", self)
                    

    @property
    def zlvp_Lager63(self):
        return self.__zlvp_Lager63

    @zlvp_Lager63.setter
    def zlvp_Lager63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Lager__zlvp_Lager63", None)
        self.__zlvp_Lager63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Lagerort62"):
                opp_val = getattr(old_value, "zlvp_Lagerort62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Lagerort62"):
                opp_val = getattr(value, "zlvp_Lagerort62", None)
                if opp_val is None:
                    setattr(value, "zlvp_Lagerort62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def zlvp_Lager(self):
        return self.__zlvp_Lager

    @zlvp_Lager.setter
    def zlvp_Lager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Lager__zlvp_Lager", None)
        self.__zlvp_Lager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Stab"):
                opp_val = getattr(old_value, "zlvp_Stab", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Stab"):
                opp_val = getattr(value, "zlvp_Stab", None)
                if opp_val is None:
                    setattr(value, "zlvp_Stab", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def zlvp_Lager31(self):
        return self.__zlvp_Lager31

    @zlvp_Lager31.setter
    def zlvp_Lager31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Lager__zlvp_Lager31", None)
        self.__zlvp_Lager31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Zelt"):
                    opp_val = getattr(item, "zlvp_Zelt", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Zelt", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Zelt"):
                    opp_val = getattr(item, "zlvp_Zelt", None)
                    
                    setattr(item, "zlvp_Zelt", self)
                    

    @property
    def zlvp_Lager24(self):
        return self.__zlvp_Lager24

    @zlvp_Lager24.setter
    def zlvp_Lager24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Lager__zlvp_Lager24", None)
        self.__zlvp_Lager24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Stab25"):
                    opp_val = getattr(item, "zlvp_Stab25", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Stab25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Stab25"):
                    opp_val = getattr(item, "zlvp_Stab25", None)
                    
                    setattr(item, "zlvp_Stab25", self)
                    

    @property
    def zlvp_Lager51(self):
        return self.__zlvp_Lager51

    @zlvp_Lager51.setter
    def zlvp_Lager51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Lager__zlvp_Lager51", None)
        self.__zlvp_Lager51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Zelt50"):
                opp_val = getattr(old_value, "zlvp_Zelt50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Zelt50"):
                opp_val = getattr(value, "zlvp_Zelt50", None)
                if opp_val is None:
                    setattr(value, "zlvp_Zelt50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def zlvp_Lager36(self):
        return self.__zlvp_Lager36

    @zlvp_Lager36.setter
    def zlvp_Lager36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Lager__zlvp_Lager36", None)
        self.__zlvp_Lager36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Lagerort"):
                opp_val = getattr(old_value, "zlvp_Lagerort", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Lagerort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Lagerort"):
                opp_val = getattr(value, "zlvp_Lagerort", None)
                setattr(value, "zlvp_Lagerort", self)

    @property
    def zlvp_Lager27(self):
        return self.__zlvp_Lager27

    @zlvp_Lager27.setter
    def zlvp_Lager27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Lager__zlvp_Lager27", None)
        self.__zlvp_Lager27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Essen"):
                    opp_val = getattr(item, "zlvp_Essen", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Essen", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Essen"):
                    opp_val = getattr(item, "zlvp_Essen", None)
                    
                    setattr(item, "zlvp_Essen", self)
                    

    @property
    def zlvp_Lager19(self):
        return self.__zlvp_Lager19

    @zlvp_Lager19.setter
    def zlvp_Lager19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Lager__zlvp_Lager19", None)
        self.__zlvp_Lager19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Jahr"):
                opp_val = getattr(old_value, "zlvp_Jahr", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Jahr"):
                opp_val = getattr(value, "zlvp_Jahr", None)
                if opp_val is None:
                    setattr(value, "zlvp_Jahr", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def zlvp_Lager21(self):
        return self.__zlvp_Lager21

    @zlvp_Lager21.setter
    def zlvp_Lager21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Lager__zlvp_Lager21", None)
        self.__zlvp_Lager21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Gruppen22"):
                    opp_val = getattr(item, "zlvp_Gruppen22", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Gruppen22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Gruppen22"):
                    opp_val = getattr(item, "zlvp_Gruppen22", None)
                    
                    setattr(item, "zlvp_Gruppen22", self)
                    

    @property
    def zlvp_Lager33(self):
        return self.__zlvp_Lager33

    @zlvp_Lager33.setter
    def zlvp_Lager33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Lager__zlvp_Lager33", None)
        self.__zlvp_Lager33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Person34"):
                    opp_val = getattr(item, "zlvp_Person34", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Person34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Person34"):
                    opp_val = getattr(item, "zlvp_Person34", None)
                    
                    setattr(item, "zlvp_Person34", self)
                    

class zlvp_Teilnehmer:

    def __init__(self, id: int, zlvp_Teilnehmer: set["zlvp_Gruppen"] = None, zlvp_Teilnehmer16: "zlvp_Person" = None, zlvp_Teilnehmer42: "zlvp_Gruppen" = None):
        self.id = id
        self.zlvp_Teilnehmer = zlvp_Teilnehmer if zlvp_Teilnehmer is not None else set()
        self.zlvp_Teilnehmer16 = zlvp_Teilnehmer16
        self.zlvp_Teilnehmer42 = zlvp_Teilnehmer42
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def zlvp_Teilnehmer(self):
        return self.__zlvp_Teilnehmer

    @zlvp_Teilnehmer.setter
    def zlvp_Teilnehmer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Teilnehmer__zlvp_Teilnehmer", None)
        self.__zlvp_Teilnehmer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Gruppen14"):
                    opp_val = getattr(item, "zlvp_Gruppen14", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Gruppen14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Gruppen14"):
                    opp_val = getattr(item, "zlvp_Gruppen14", None)
                    
                    setattr(item, "zlvp_Gruppen14", self)
                    

    @property
    def zlvp_Teilnehmer16(self):
        return self.__zlvp_Teilnehmer16

    @zlvp_Teilnehmer16.setter
    def zlvp_Teilnehmer16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Teilnehmer__zlvp_Teilnehmer16", None)
        self.__zlvp_Teilnehmer16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Person17"):
                opp_val = getattr(old_value, "zlvp_Person17", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Person17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Person17"):
                opp_val = getattr(value, "zlvp_Person17", None)
                setattr(value, "zlvp_Person17", self)

    @property
    def zlvp_Teilnehmer42(self):
        return self.__zlvp_Teilnehmer42

    @zlvp_Teilnehmer42.setter
    def zlvp_Teilnehmer42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Teilnehmer__zlvp_Teilnehmer42", None)
        self.__zlvp_Teilnehmer42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Gruppen41"):
                opp_val = getattr(old_value, "zlvp_Gruppen41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Gruppen41"):
                opp_val = getattr(value, "zlvp_Gruppen41", None)
                if opp_val is None:
                    setattr(value, "zlvp_Gruppen41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class zlvp_Gruppen:

    def __init__(self, id: int, name: str, spruch: str, zlvp_Gruppen: "zlvp_Leiter" = None, zlvp_Gruppen14: "zlvp_Teilnehmer" = None, zlvp_Gruppen22: "zlvp_Lager" = None, zlvp_Gruppen38: set["zlvp_Leiter"] = None, zlvp_Gruppen41: set["zlvp_Teilnehmer"] = None):
        self.id = id
        self.name = name
        self.spruch = spruch
        self.zlvp_Gruppen = zlvp_Gruppen
        self.zlvp_Gruppen14 = zlvp_Gruppen14
        self.zlvp_Gruppen22 = zlvp_Gruppen22
        self.zlvp_Gruppen38 = zlvp_Gruppen38 if zlvp_Gruppen38 is not None else set()
        self.zlvp_Gruppen41 = zlvp_Gruppen41 if zlvp_Gruppen41 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def spruch(self) -> str:
        return self.__spruch

    @spruch.setter
    def spruch(self, spruch: str):
        self.__spruch = spruch

    @property
    def zlvp_Gruppen14(self):
        return self.__zlvp_Gruppen14

    @zlvp_Gruppen14.setter
    def zlvp_Gruppen14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Gruppen__zlvp_Gruppen14", None)
        self.__zlvp_Gruppen14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Teilnehmer"):
                opp_val = getattr(old_value, "zlvp_Teilnehmer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Teilnehmer"):
                opp_val = getattr(value, "zlvp_Teilnehmer", None)
                if opp_val is None:
                    setattr(value, "zlvp_Teilnehmer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def zlvp_Gruppen41(self):
        return self.__zlvp_Gruppen41

    @zlvp_Gruppen41.setter
    def zlvp_Gruppen41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Gruppen__zlvp_Gruppen41", None)
        self.__zlvp_Gruppen41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Teilnehmer42"):
                    opp_val = getattr(item, "zlvp_Teilnehmer42", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Teilnehmer42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Teilnehmer42"):
                    opp_val = getattr(item, "zlvp_Teilnehmer42", None)
                    
                    setattr(item, "zlvp_Teilnehmer42", self)
                    

    @property
    def zlvp_Gruppen38(self):
        return self.__zlvp_Gruppen38

    @zlvp_Gruppen38.setter
    def zlvp_Gruppen38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Gruppen__zlvp_Gruppen38", None)
        self.__zlvp_Gruppen38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Leiter39"):
                    opp_val = getattr(item, "zlvp_Leiter39", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Leiter39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Leiter39"):
                    opp_val = getattr(item, "zlvp_Leiter39", None)
                    
                    setattr(item, "zlvp_Leiter39", self)
                    

    @property
    def zlvp_Gruppen22(self):
        return self.__zlvp_Gruppen22

    @zlvp_Gruppen22.setter
    def zlvp_Gruppen22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Gruppen__zlvp_Gruppen22", None)
        self.__zlvp_Gruppen22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Lager21"):
                opp_val = getattr(old_value, "zlvp_Lager21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Lager21"):
                opp_val = getattr(value, "zlvp_Lager21", None)
                if opp_val is None:
                    setattr(value, "zlvp_Lager21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def zlvp_Gruppen(self):
        return self.__zlvp_Gruppen

    @zlvp_Gruppen.setter
    def zlvp_Gruppen(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Gruppen__zlvp_Gruppen", None)
        self.__zlvp_Gruppen = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Leiter"):
                opp_val = getattr(old_value, "zlvp_Leiter", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Leiter"):
                opp_val = getattr(value, "zlvp_Leiter", None)
                if opp_val is None:
                    setattr(value, "zlvp_Leiter", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class zlvp_Leiter:

    def __init__(self, id: int, zlvp_Leiter: set["zlvp_Gruppen"] = None, zlvp_Leiter11: "zlvp_Person" = None, zlvp_Leiter39: "zlvp_Gruppen" = None):
        self.id = id
        self.zlvp_Leiter = zlvp_Leiter if zlvp_Leiter is not None else set()
        self.zlvp_Leiter11 = zlvp_Leiter11
        self.zlvp_Leiter39 = zlvp_Leiter39
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def zlvp_Leiter39(self):
        return self.__zlvp_Leiter39

    @zlvp_Leiter39.setter
    def zlvp_Leiter39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Leiter__zlvp_Leiter39", None)
        self.__zlvp_Leiter39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Gruppen38"):
                opp_val = getattr(old_value, "zlvp_Gruppen38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Gruppen38"):
                opp_val = getattr(value, "zlvp_Gruppen38", None)
                if opp_val is None:
                    setattr(value, "zlvp_Gruppen38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def zlvp_Leiter11(self):
        return self.__zlvp_Leiter11

    @zlvp_Leiter11.setter
    def zlvp_Leiter11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Leiter__zlvp_Leiter11", None)
        self.__zlvp_Leiter11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Person12"):
                opp_val = getattr(old_value, "zlvp_Person12", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Person12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Person12"):
                opp_val = getattr(value, "zlvp_Person12", None)
                setattr(value, "zlvp_Person12", self)

    @property
    def zlvp_Leiter(self):
        return self.__zlvp_Leiter

    @zlvp_Leiter.setter
    def zlvp_Leiter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Leiter__zlvp_Leiter", None)
        self.__zlvp_Leiter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Gruppen"):
                    opp_val = getattr(item, "zlvp_Gruppen", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Gruppen", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Gruppen"):
                    opp_val = getattr(item, "zlvp_Gruppen", None)
                    
                    setattr(item, "zlvp_Gruppen", self)
                    

class zlvp_Funktion:

    def __init__(self, id: int, name: str, zlvp_Funktion: "zlvp_Stab" = None):
        self.id = id
        self.name = name
        self.zlvp_Funktion = zlvp_Funktion
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def zlvp_Funktion(self):
        return self.__zlvp_Funktion

    @zlvp_Funktion.setter
    def zlvp_Funktion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Funktion__zlvp_Funktion", None)
        self.__zlvp_Funktion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Stab8"):
                opp_val = getattr(old_value, "zlvp_Stab8", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Stab8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Stab8"):
                opp_val = getattr(value, "zlvp_Stab8", None)
                setattr(value, "zlvp_Stab8", self)

class zlvp_Stab:

    def __init__(self, id: int, zlvp_Stab5: "zlvp_Person" = None, zlvp_Stab8: "zlvp_Funktion" = None, zlvp_Stab: set["zlvp_Lager"] = None, zlvp_Stab25: "zlvp_Lager" = None):
        self.id = id
        self.zlvp_Stab5 = zlvp_Stab5
        self.zlvp_Stab8 = zlvp_Stab8
        self.zlvp_Stab = zlvp_Stab if zlvp_Stab is not None else set()
        self.zlvp_Stab25 = zlvp_Stab25
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def zlvp_Stab(self):
        return self.__zlvp_Stab

    @zlvp_Stab.setter
    def zlvp_Stab(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Stab__zlvp_Stab", None)
        self.__zlvp_Stab = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zlvp_Lager"):
                    opp_val = getattr(item, "zlvp_Lager", None)
                    
                    if opp_val == self:
                        setattr(item, "zlvp_Lager", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zlvp_Lager"):
                    opp_val = getattr(item, "zlvp_Lager", None)
                    
                    setattr(item, "zlvp_Lager", self)
                    

    @property
    def zlvp_Stab25(self):
        return self.__zlvp_Stab25

    @zlvp_Stab25.setter
    def zlvp_Stab25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Stab__zlvp_Stab25", None)
        self.__zlvp_Stab25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Lager24"):
                opp_val = getattr(old_value, "zlvp_Lager24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Lager24"):
                opp_val = getattr(value, "zlvp_Lager24", None)
                if opp_val is None:
                    setattr(value, "zlvp_Lager24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def zlvp_Stab5(self):
        return self.__zlvp_Stab5

    @zlvp_Stab5.setter
    def zlvp_Stab5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Stab__zlvp_Stab5", None)
        self.__zlvp_Stab5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Person6"):
                opp_val = getattr(old_value, "zlvp_Person6", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Person6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Person6"):
                opp_val = getattr(value, "zlvp_Person6", None)
                setattr(value, "zlvp_Person6", self)

    @property
    def zlvp_Stab8(self):
        return self.__zlvp_Stab8

    @zlvp_Stab8.setter
    def zlvp_Stab8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Stab__zlvp_Stab8", None)
        self.__zlvp_Stab8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Funktion"):
                opp_val = getattr(old_value, "zlvp_Funktion", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Funktion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Funktion"):
                opp_val = getattr(value, "zlvp_Funktion", None)
                setattr(value, "zlvp_Funktion", self)

class zlvp_Anrede:

    def __init__(self, id: int, name: str, zlvp_Anrede: "zlvp_Person" = None, zlvp_Anrede55: "zlvp_Legenda" = None):
        self.id = id
        self.name = name
        self.zlvp_Anrede = zlvp_Anrede
        self.zlvp_Anrede55 = zlvp_Anrede55
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def zlvp_Anrede55(self):
        return self.__zlvp_Anrede55

    @zlvp_Anrede55.setter
    def zlvp_Anrede55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Anrede__zlvp_Anrede55", None)
        self.__zlvp_Anrede55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Legenda"):
                opp_val = getattr(old_value, "zlvp_Legenda", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Legenda", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Legenda"):
                opp_val = getattr(value, "zlvp_Legenda", None)
                setattr(value, "zlvp_Legenda", self)

    @property
    def zlvp_Anrede(self):
        return self.__zlvp_Anrede

    @zlvp_Anrede.setter
    def zlvp_Anrede(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Anrede__zlvp_Anrede", None)
        self.__zlvp_Anrede = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Person2"):
                opp_val = getattr(old_value, "zlvp_Person2", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Person2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Person2"):
                opp_val = getattr(value, "zlvp_Person2", None)
                setattr(value, "zlvp_Person2", self)

class zlvp_Person:

    def __init__(self, id: int, nachname: str, vorname: str, strasse: str, plz: str, ort: str, telNr: str, handyNr: str, email: str, gebDat: date, notTelNr: str, version: str, zlvp_Person2: "zlvp_Anrede" = None, zlvp_Person: "zlvp_Geschlecht" = None, zlvp_Person6: "zlvp_Stab" = None, zlvp_Person12: "zlvp_Leiter" = None, zlvp_Person17: "zlvp_Teilnehmer" = None, zlvp_Person34: "zlvp_Lager" = None):
        self.id = id
        self.nachname = nachname
        self.vorname = vorname
        self.strasse = strasse
        self.plz = plz
        self.ort = ort
        self.telNr = telNr
        self.handyNr = handyNr
        self.email = email
        self.gebDat = gebDat
        self.notTelNr = notTelNr
        self.version = version
        self.zlvp_Person2 = zlvp_Person2
        self.zlvp_Person = zlvp_Person
        self.zlvp_Person6 = zlvp_Person6
        self.zlvp_Person12 = zlvp_Person12
        self.zlvp_Person17 = zlvp_Person17
        self.zlvp_Person34 = zlvp_Person34
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def strasse(self) -> str:
        return self.__strasse

    @strasse.setter
    def strasse(self, strasse: str):
        self.__strasse = strasse

    @property
    def ort(self) -> str:
        return self.__ort

    @ort.setter
    def ort(self, ort: str):
        self.__ort = ort

    @property
    def gebDat(self) -> date:
        return self.__gebDat

    @gebDat.setter
    def gebDat(self, gebDat: date):
        self.__gebDat = gebDat

    @property
    def nachname(self) -> str:
        return self.__nachname

    @nachname.setter
    def nachname(self, nachname: str):
        self.__nachname = nachname

    @property
    def plz(self) -> str:
        return self.__plz

    @plz.setter
    def plz(self, plz: str):
        self.__plz = plz

    @property
    def handyNr(self) -> str:
        return self.__handyNr

    @handyNr.setter
    def handyNr(self, handyNr: str):
        self.__handyNr = handyNr

    @property
    def vorname(self) -> str:
        return self.__vorname

    @vorname.setter
    def vorname(self, vorname: str):
        self.__vorname = vorname

    @property
    def notTelNr(self) -> str:
        return self.__notTelNr

    @notTelNr.setter
    def notTelNr(self, notTelNr: str):
        self.__notTelNr = notTelNr

    @property
    def telNr(self) -> str:
        return self.__telNr

    @telNr.setter
    def telNr(self, telNr: str):
        self.__telNr = telNr

    @property
    def zlvp_Person(self):
        return self.__zlvp_Person

    @zlvp_Person.setter
    def zlvp_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Person__zlvp_Person", None)
        self.__zlvp_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Geschlecht"):
                opp_val = getattr(old_value, "zlvp_Geschlecht", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Geschlecht", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Geschlecht"):
                opp_val = getattr(value, "zlvp_Geschlecht", None)
                setattr(value, "zlvp_Geschlecht", self)

    @property
    def zlvp_Person12(self):
        return self.__zlvp_Person12

    @zlvp_Person12.setter
    def zlvp_Person12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Person__zlvp_Person12", None)
        self.__zlvp_Person12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Leiter11"):
                opp_val = getattr(old_value, "zlvp_Leiter11", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Leiter11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Leiter11"):
                opp_val = getattr(value, "zlvp_Leiter11", None)
                setattr(value, "zlvp_Leiter11", self)

    @property
    def zlvp_Person6(self):
        return self.__zlvp_Person6

    @zlvp_Person6.setter
    def zlvp_Person6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Person__zlvp_Person6", None)
        self.__zlvp_Person6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Stab5"):
                opp_val = getattr(old_value, "zlvp_Stab5", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Stab5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Stab5"):
                opp_val = getattr(value, "zlvp_Stab5", None)
                setattr(value, "zlvp_Stab5", self)

    @property
    def zlvp_Person17(self):
        return self.__zlvp_Person17

    @zlvp_Person17.setter
    def zlvp_Person17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Person__zlvp_Person17", None)
        self.__zlvp_Person17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Teilnehmer16"):
                opp_val = getattr(old_value, "zlvp_Teilnehmer16", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Teilnehmer16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Teilnehmer16"):
                opp_val = getattr(value, "zlvp_Teilnehmer16", None)
                setattr(value, "zlvp_Teilnehmer16", self)

    @property
    def zlvp_Person2(self):
        return self.__zlvp_Person2

    @zlvp_Person2.setter
    def zlvp_Person2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Person__zlvp_Person2", None)
        self.__zlvp_Person2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Anrede"):
                opp_val = getattr(old_value, "zlvp_Anrede", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Anrede", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Anrede"):
                opp_val = getattr(value, "zlvp_Anrede", None)
                setattr(value, "zlvp_Anrede", self)

    @property
    def zlvp_Person34(self):
        return self.__zlvp_Person34

    @zlvp_Person34.setter
    def zlvp_Person34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Person__zlvp_Person34", None)
        self.__zlvp_Person34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Lager33"):
                opp_val = getattr(old_value, "zlvp_Lager33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Lager33"):
                opp_val = getattr(value, "zlvp_Lager33", None)
                if opp_val is None:
                    setattr(value, "zlvp_Lager33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class zlvp_Geschlecht:

    def __init__(self, id: int, name: str, zlvp_Geschlecht: "zlvp_Person" = None):
        self.id = id
        self.name = name
        self.zlvp_Geschlecht = zlvp_Geschlecht
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def zlvp_Geschlecht(self):
        return self.__zlvp_Geschlecht

    @zlvp_Geschlecht.setter
    def zlvp_Geschlecht(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zlvp_Geschlecht__zlvp_Geschlecht", None)
        self.__zlvp_Geschlecht = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zlvp_Person"):
                opp_val = getattr(old_value, "zlvp_Person", None)
                if opp_val == self:
                    setattr(old_value, "zlvp_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zlvp_Person"):
                opp_val = getattr(value, "zlvp_Person", None)
                setattr(value, "zlvp_Person", self)
