from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class retard:

    def __init__(self, motif: str, idretad: int, nbrminute: int, employ_12: "Employ_" = None):
        self.motif = motif
        self.idretad = idretad
        self.nbrminute = nbrminute
        self.employ_12 = employ_12
        
        pass
    @property
    def nbrminute(self):
        return self.__nbrminute
    @nbrminute.setter
    def nbrminute(self, nbrminute: int):
        self.__nbrminute = nbrminute

    @property
    def motif(self):
        return self.__motif
    @motif.setter
    def motif(self, motif: str):
        self.__motif = motif

    @property
    def idretad(self):
        return self.__idretad
    @idretad.setter
    def idretad(self, idretad: int):
        self.__idretad = idretad

    @property
    def employ_12(self):
        return self.__employ_12
    @employ_12.setter
    def employ_12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_retard__employ_12", None)
        self.__employ_12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "retard13"):
                opp_val = getattr(old_value, "retard13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "retard13"):
                opp_val = getattr(value, "retard13", None)
                if opp_val is None:
                    setattr(value, "retard13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class abs:

    def __init__(self, idab: int, nbrjr: int, motif: str, employ_10: "Employ_" = None):
        self.idab = idab
        self.nbrjr = nbrjr
        self.motif = motif
        self.employ_10 = employ_10
        
        pass
    @property
    def motif(self):
        return self.__motif
    @motif.setter
    def motif(self, motif: str):
        self.__motif = motif

    @property
    def nbrjr(self):
        return self.__nbrjr
    @nbrjr.setter
    def nbrjr(self, nbrjr: int):
        self.__nbrjr = nbrjr

    @property
    def idab(self):
        return self.__idab
    @idab.setter
    def idab(self, idab: int):
        self.__idab = idab

    @property
    def employ_10(self):
        return self.__employ_10
    @employ_10.setter
    def employ_10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abs__employ_10", None)
        self.__employ_10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abs11"):
                opp_val = getattr(old_value, "abs11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abs11"):
                opp_val = getattr(value, "abs11", None)
                if opp_val is None:
                    setattr(value, "abs11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class reduire:

    pass


class EtatConge:

    def __init__(self, idEtat: int, nom: str, conge9: set["Conge"] = None):
        self.idEtat = idEtat
        self.nom = nom
        self.conge9 = conge9 if conge9 is not None else set()
        
        pass
    @property
    def idEtat(self):
        return self.__idEtat
    @idEtat.setter
    def idEtat(self, idEtat: int):
        self.__idEtat = idEtat

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def conge9(self):
        return self.__conge9
    @conge9.setter
    def conge9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EtatConge__conge9", None)
        self.__conge9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etatConge8"):
                    opp_val = getattr(item, "etatConge8", None)
                    
                    if opp_val == self:
                        setattr(item, "etatConge8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etatConge8"):
                    opp_val = getattr(item, "etatConge8", None)
                    
                    setattr(item, "etatConge8", self)
                    



class typecong_:

    def __init__(self, idconge: int, conge7: set["Conge"] = None):
        self.idconge = idconge
        self.conge7 = conge7 if conge7 is not None else set()
        
        pass
    @property
    def idconge(self):
        return self.__idconge
    @idconge.setter
    def idconge(self, idconge: int):
        self.__idconge = idconge

    @property
    def conge7(self):
        return self.__conge7
    @conge7.setter
    def conge7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typecong___conge7", None)
        self.__conge7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "typecong_6"):
                    opp_val = getattr(item, "typecong_6", None)
                    
                    if opp_val == self:
                        setattr(item, "typecong_6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "typecong_6"):
                    opp_val = getattr(item, "typecong_6", None)
                    
                    setattr(item, "typecong_6", self)
                    



class Conge:

    def __init__(self, id: int, datedebut: str, datefin: str, adresse: str, employ_3: set["Employ_"] = None, salari_5: set["salari_"] = None, typecong_6: "typecong_" = None, etatConge8: "EtatConge" = None):
        self.id = id
        self.datedebut = datedebut
        self.datefin = datefin
        self.adresse = adresse
        self.employ_3 = employ_3 if employ_3 is not None else set()
        self.salari_5 = salari_5 if salari_5 is not None else set()
        self.typecong_6 = typecong_6
        self.etatConge8 = etatConge8
        
        pass
    @property
    def adresse(self):
        return self.__adresse
    @adresse.setter
    def adresse(self, adresse: str):
        self.__adresse = adresse

    @property
    def datedebut(self):
        return self.__datedebut
    @datedebut.setter
    def datedebut(self, datedebut: str):
        self.__datedebut = datedebut

    @property
    def datefin(self):
        return self.__datefin
    @datefin.setter
    def datefin(self, datefin: str):
        self.__datefin = datefin

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def employ_3(self):
        return self.__employ_3
    @employ_3.setter
    def employ_3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Conge__employ_3", None)
        self.__employ_3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conge2"):
                    opp_val = getattr(item, "conge2", None)
                    
                    if opp_val == self:
                        setattr(item, "conge2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conge2"):
                    opp_val = getattr(item, "conge2", None)
                    
                    setattr(item, "conge2", self)
                    

    @property
    def typecong_6(self):
        return self.__typecong_6
    @typecong_6.setter
    def typecong_6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Conge__typecong_6", None)
        self.__typecong_6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conge7"):
                opp_val = getattr(old_value, "conge7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conge7"):
                opp_val = getattr(value, "conge7", None)
                if opp_val is None:
                    setattr(value, "conge7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def salari_5(self):
        return self.__salari_5
    @salari_5.setter
    def salari_5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Conge__salari_5", None)
        self.__salari_5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conge4"):
                    opp_val = getattr(item, "conge4", None)
                    
                    if opp_val == self:
                        setattr(item, "conge4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conge4"):
                    opp_val = getattr(item, "conge4", None)
                    
                    setattr(item, "conge4", self)
                    

    @property
    def etatConge8(self):
        return self.__etatConge8
    @etatConge8.setter
    def etatConge8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Conge__etatConge8", None)
        self.__etatConge8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conge9"):
                opp_val = getattr(old_value, "conge9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conge9"):
                opp_val = getattr(value, "conge9", None)
                if opp_val is None:
                    setattr(value, "conge9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class typeEmploy_:

    def __init__(self, id: str, employ_1: set["Employ_"] = None):
        self.id = id
        self.employ_1 = employ_1 if employ_1 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def employ_1(self):
        return self.__employ_1
    @employ_1.setter
    def employ_1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeEmploy___employ_1", None)
        self.__employ_1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "typeEmploy_0"):
                    opp_val = getattr(item, "typeEmploy_0", None)
                    
                    if opp_val == self:
                        setattr(item, "typeEmploy_0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "typeEmploy_0"):
                    opp_val = getattr(item, "typeEmploy_0", None)
                    
                    setattr(item, "typeEmploy_0", self)
                    



class salari_:

    def __init__(self, departement: str, conge4: "Conge" = None):
        self.departement = departement
        self.conge4 = conge4
        
        pass
    @property
    def departement(self):
        return self.__departement
    @departement.setter
    def departement(self, departement: str):
        self.__departement = departement

    @property
    def conge4(self):
        return self.__conge4
    @conge4.setter
    def conge4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_salari___conge4", None)
        self.__conge4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "salari_5"):
                opp_val = getattr(old_value, "salari_5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "salari_5"):
                opp_val = getattr(value, "salari_5", None)
                if opp_val is None:
                    setattr(value, "salari_5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class administrateur:

    def __init__(self, secteur: str):
        self.secteur = secteur
        
        pass
    @property
    def secteur(self):
        return self.__secteur
    @secteur.setter
    def secteur(self, secteur: str):
        self.__secteur = secteur



class Employ_:

    def __init__(self, ID: int, nom: str, prenom: str, poste: str, adresse: str, typeEmploy_0: "typeEmploy_" = None, conge2: "Conge" = None, abs11: set["abs"] = None, retard13: set["retard"] = None):
        self.ID = ID
        self.nom = nom
        self.prenom = prenom
        self.poste = poste
        self.adresse = adresse
        self.typeEmploy_0 = typeEmploy_0
        self.conge2 = conge2
        self.abs11 = abs11 if abs11 is not None else set()
        self.retard13 = retard13 if retard13 is not None else set()
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def adresse(self):
        return self.__adresse
    @adresse.setter
    def adresse(self, adresse: str):
        self.__adresse = adresse

    @property
    def poste(self):
        return self.__poste
    @poste.setter
    def poste(self, poste: str):
        self.__poste = poste

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, prenom: str):
        self.__prenom = prenom

    @property
    def conge2(self):
        return self.__conge2
    @conge2.setter
    def conge2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employ___conge2", None)
        self.__conge2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employ_3"):
                opp_val = getattr(old_value, "employ_3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employ_3"):
                opp_val = getattr(value, "employ_3", None)
                if opp_val is None:
                    setattr(value, "employ_3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def retard13(self):
        return self.__retard13
    @retard13.setter
    def retard13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employ___retard13", None)
        self.__retard13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employ_12"):
                    opp_val = getattr(item, "employ_12", None)
                    
                    if opp_val == self:
                        setattr(item, "employ_12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employ_12"):
                    opp_val = getattr(item, "employ_12", None)
                    
                    setattr(item, "employ_12", self)
                    

    @property
    def abs11(self):
        return self.__abs11
    @abs11.setter
    def abs11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employ___abs11", None)
        self.__abs11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employ_10"):
                    opp_val = getattr(item, "employ_10", None)
                    
                    if opp_val == self:
                        setattr(item, "employ_10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employ_10"):
                    opp_val = getattr(item, "employ_10", None)
                    
                    setattr(item, "employ_10", self)
                    

    @property
    def typeEmploy_0(self):
        return self.__typeEmploy_0
    @typeEmploy_0.setter
    def typeEmploy_0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employ___typeEmploy_0", None)
        self.__typeEmploy_0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employ_1"):
                opp_val = getattr(old_value, "employ_1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employ_1"):
                opp_val = getattr(value, "employ_1", None)
                if opp_val is None:
                    setattr(value, "employ_1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

