from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Participant:

    def __init__(self, id_session: int, nom: str, prenom: str, date_naissance: str, sessions1: set["Prestation"] = None):
        self.id_session = id_session
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sessions1 = sessions1 if sessions1 is not None else set()
        
        pass
    @property
    def id_session(self):
        return self.__id_session
    @id_session.setter
    def id_session(self, id_session: int):
        self.__id_session = id_session

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def date_naissance(self):
        return self.__date_naissance
    @date_naissance.setter
    def date_naissance(self, date_naissance: str):
        self.__date_naissance = date_naissance

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, prenom: str):
        self.__prenom = prenom

    @property
    def sessions1(self):
        return self.__sessions1
    @sessions1.setter
    def sessions1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Participant__sessions1", None)
        self.__sessions1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "participants0"):
                    opp_val = getattr(item, "participants0", None)
                    
                    if opp_val == self:
                        setattr(item, "participants0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "participants0"):
                    opp_val = getattr(item, "participants0", None)
                    
                    setattr(item, "participants0", self)
                    



class Formateur:

    def __init__(self, Nom: str, Prenom: str, sessions2: "Prestation" = None):
        self.Nom = Nom
        self.Prenom = Prenom
        self.sessions2 = sessions2
        
        pass
    @property
    def Prenom(self):
        return self.__Prenom
    @Prenom.setter
    def Prenom(self, Prenom: str):
        self.__Prenom = Prenom

    @property
    def Nom(self):
        return self.__Nom
    @Nom.setter
    def Nom(self, Nom: str):
        self.__Nom = Nom

    @property
    def sessions2(self):
        return self.__sessions2
    @sessions2.setter
    def sessions2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Formateur__sessions2", None)
        self.__sessions2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "formateurs3"):
                opp_val = getattr(old_value, "formateurs3", None)
                if opp_val == self:
                    setattr(old_value, "formateurs3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "formateurs3"):
                opp_val = getattr(value, "formateurs3", None)
                setattr(value, "formateurs3", self)



class Prestation:

    def __init__(self, id_client: int, id_formation: int, id_formateur: int, id_type: int, date_debut: str, date_fin: str, duree: str, horaires: str, lieu: bool, nb_stagiaires: int, participants0: "Participant" = None, formateurs3: "Formateur" = None, devisEntete5: "DevisEntete" = None, client7: "Client" = None, formation9: "Formation" = None, type11: "Type" = None):
        self.id_client = id_client
        self.id_formation = id_formation
        self.id_formateur = id_formateur
        self.id_type = id_type
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.duree = duree
        self.horaires = horaires
        self.lieu = lieu
        self.nb_stagiaires = nb_stagiaires
        self.participants0 = participants0
        self.formateurs3 = formateurs3
        self.devisEntete5 = devisEntete5
        self.client7 = client7
        self.formation9 = formation9
        self.type11 = type11
        
        pass
    @property
    def date_debut(self):
        return self.__date_debut
    @date_debut.setter
    def date_debut(self, date_debut: str):
        self.__date_debut = date_debut

    @property
    def duree(self):
        return self.__duree
    @duree.setter
    def duree(self, duree: str):
        self.__duree = duree

    @property
    def id_client(self):
        return self.__id_client
    @id_client.setter
    def id_client(self, id_client: int):
        self.__id_client = id_client

    @property
    def horaires(self):
        return self.__horaires
    @horaires.setter
    def horaires(self, horaires: str):
        self.__horaires = horaires

    @property
    def lieu(self):
        return self.__lieu
    @lieu.setter
    def lieu(self, lieu: bool):
        self.__lieu = lieu

    @property
    def id_type(self):
        return self.__id_type
    @id_type.setter
    def id_type(self, id_type: int):
        self.__id_type = id_type

    @property
    def nb_stagiaires(self):
        return self.__nb_stagiaires
    @nb_stagiaires.setter
    def nb_stagiaires(self, nb_stagiaires: int):
        self.__nb_stagiaires = nb_stagiaires

    @property
    def id_formateur(self):
        return self.__id_formateur
    @id_formateur.setter
    def id_formateur(self, id_formateur: int):
        self.__id_formateur = id_formateur

    @property
    def id_formation(self):
        return self.__id_formation
    @id_formation.setter
    def id_formation(self, id_formation: int):
        self.__id_formation = id_formation

    @property
    def date_fin(self):
        return self.__date_fin
    @date_fin.setter
    def date_fin(self, date_fin: str):
        self.__date_fin = date_fin

    @property
    def client7(self):
        return self.__client7
    @client7.setter
    def client7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Prestation__client7", None)
        self.__client7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "session6"):
                opp_val = getattr(old_value, "session6", None)
                if opp_val == self:
                    setattr(old_value, "session6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "session6"):
                opp_val = getattr(value, "session6", None)
                setattr(value, "session6", self)

    @property
    def participants0(self):
        return self.__participants0
    @participants0.setter
    def participants0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Prestation__participants0", None)
        self.__participants0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sessions1"):
                opp_val = getattr(old_value, "sessions1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sessions1"):
                opp_val = getattr(value, "sessions1", None)
                if opp_val is None:
                    setattr(value, "sessions1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def formateurs3(self):
        return self.__formateurs3
    @formateurs3.setter
    def formateurs3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Prestation__formateurs3", None)
        self.__formateurs3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sessions2"):
                opp_val = getattr(old_value, "sessions2", None)
                if opp_val == self:
                    setattr(old_value, "sessions2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sessions2"):
                opp_val = getattr(value, "sessions2", None)
                setattr(value, "sessions2", self)

    @property
    def formation9(self):
        return self.__formation9
    @formation9.setter
    def formation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Prestation__formation9", None)
        self.__formation9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "session8"):
                opp_val = getattr(old_value, "session8", None)
                if opp_val == self:
                    setattr(old_value, "session8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "session8"):
                opp_val = getattr(value, "session8", None)
                setattr(value, "session8", self)

    @property
    def type11(self):
        return self.__type11
    @type11.setter
    def type11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Prestation__type11", None)
        self.__type11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prestation10"):
                opp_val = getattr(old_value, "prestation10", None)
                if opp_val == self:
                    setattr(old_value, "prestation10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prestation10"):
                opp_val = getattr(value, "prestation10", None)
                setattr(value, "prestation10", self)

    @property
    def devisEntete5(self):
        return self.__devisEntete5
    @devisEntete5.setter
    def devisEntete5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Prestation__devisEntete5", None)
        self.__devisEntete5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "session4"):
                opp_val = getattr(old_value, "session4", None)
                if opp_val == self:
                    setattr(old_value, "session4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "session4"):
                opp_val = getattr(value, "session4", None)
                setattr(value, "session4", self)



class Type:

    def __init__(self, type: str, prestation10: "Prestation" = None):
        self.type = type
        self.prestation10 = prestation10
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def prestation10(self):
        return self.__prestation10
    @prestation10.setter
    def prestation10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Type__prestation10", None)
        self.__prestation10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type11"):
                opp_val = getattr(old_value, "type11", None)
                if opp_val == self:
                    setattr(old_value, "type11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type11"):
                opp_val = getattr(value, "type11", None)
                setattr(value, "type11", self)



class Convention:

    def __init__(self, numero: str, id_convention: int):
        self.numero = numero
        self.id_convention = id_convention
        
        pass
    @property
    def id_convention(self):
        return self.__id_convention
    @id_convention.setter
    def id_convention(self, id_convention: int):
        self.__id_convention = id_convention

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero: str):
        self.__numero = numero



class Facture:

    def __init__(self, numero: str, id_devis: int, paye: bool):
        self.numero = numero
        self.id_devis = id_devis
        self.paye = paye
        
        pass
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero: str):
        self.__numero = numero

    @property
    def paye(self):
        return self.__paye
    @paye.setter
    def paye(self, paye: bool):
        self.__paye = paye

    @property
    def id_devis(self):
        return self.__id_devis
    @id_devis.setter
    def id_devis(self, id_devis: int):
        self.__id_devis = id_devis



class DevisEntete:

    def __init__(self, numero: str, id_session: int, session4: "Prestation" = None):
        self.numero = numero
        self.id_session = id_session
        self.session4 = session4
        
        pass
    @property
    def id_session(self):
        return self.__id_session
    @id_session.setter
    def id_session(self, id_session: int):
        self.__id_session = id_session

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero: str):
        self.__numero = numero

    @property
    def session4(self):
        return self.__session4
    @session4.setter
    def session4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DevisEntete__session4", None)
        self.__session4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "devisEntete5"):
                opp_val = getattr(old_value, "devisEntete5", None)
                if opp_val == self:
                    setattr(old_value, "devisEntete5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "devisEntete5"):
                opp_val = getattr(value, "devisEntete5", None)
                setattr(value, "devisEntete5", self)



class Formation:

    def __init__(self, libelle: str, cout_unitaire: int, objectif: str, session8: "Prestation" = None):
        self.libelle = libelle
        self.cout_unitaire = cout_unitaire
        self.objectif = objectif
        self.session8 = session8
        
        pass
    @property
    def objectif(self):
        return self.__objectif
    @objectif.setter
    def objectif(self, objectif: str):
        self.__objectif = objectif

    @property
    def cout_unitaire(self):
        return self.__cout_unitaire
    @cout_unitaire.setter
    def cout_unitaire(self, cout_unitaire: int):
        self.__cout_unitaire = cout_unitaire

    @property
    def libelle(self):
        return self.__libelle
    @libelle.setter
    def libelle(self, libelle: str):
        self.__libelle = libelle

    @property
    def session8(self):
        return self.__session8
    @session8.setter
    def session8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Formation__session8", None)
        self.__session8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "formation9"):
                opp_val = getattr(old_value, "formation9", None)
                if opp_val == self:
                    setattr(old_value, "formation9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "formation9"):
                opp_val = getattr(value, "formation9", None)
                setattr(value, "formation9", self)



class Client:

    def __init__(self, nom: str, adresse: str, codePostal: str, ville: str, contact: str, tel: str, session6: "Prestation" = None):
        self.nom = nom
        self.adresse = adresse
        self.codePostal = codePostal
        self.ville = ville
        self.contact = contact
        self.tel = tel
        self.session6 = session6
        
        pass
    @property
    def codePostal(self):
        return self.__codePostal
    @codePostal.setter
    def codePostal(self, codePostal: str):
        self.__codePostal = codePostal

    @property
    def tel(self):
        return self.__tel
    @tel.setter
    def tel(self, tel: str):
        self.__tel = tel

    @property
    def ville(self):
        return self.__ville
    @ville.setter
    def ville(self, ville: str):
        self.__ville = ville

    @property
    def adresse(self):
        return self.__adresse
    @adresse.setter
    def adresse(self, adresse: str):
        self.__adresse = adresse

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self, contact: str):
        self.__contact = contact

    @property
    def session6(self):
        return self.__session6
    @session6.setter
    def session6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Client__session6", None)
        self.__session6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "client7"):
                opp_val = getattr(old_value, "client7", None)
                if opp_val == self:
                    setattr(old_value, "client7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "client7"):
                opp_val = getattr(value, "client7", None)
                setattr(value, "client7", self)

