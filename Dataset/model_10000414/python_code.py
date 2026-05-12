from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class CCP:

    def __init__(self, id_ccp: int, label: str, description: str, formation19: set["Formation"] = None):
        self.id_ccp = id_ccp
        self.label = label
        self.description = description
        self.formation19 = formation19 if formation19 is not None else set()
        
        pass
    @property
    def label(self):
        return self.__label
    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def id_ccp(self):
        return self.__id_ccp
    @id_ccp.setter
    def id_ccp(self, id_ccp: int):
        self.__id_ccp = id_ccp

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def formation19(self):
        return self.__formation19
    @formation19.setter
    def formation19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CCP__formation19", None)
        self.__formation19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cCP18"):
                    opp_val = getattr(item, "cCP18", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cCP18"):
                    opp_val = getattr(item, "cCP18", None)
                    
                    if opp_val is None:
                        setattr(item, "cCP18", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Document:

    def __init__(self, id_document: int, label: str, descriptif: str, url: str, cours: bool, session20: set["Session"] = None):
        self.id_document = id_document
        self.label = label
        self.descriptif = descriptif
        self.url = url
        self.cours = cours
        self.session20 = session20 if session20 is not None else set()
        
        pass
    @property
    def cours(self):
        return self.__cours
    @cours.setter
    def cours(self, cours: bool):
        self.__cours = cours

    @property
    def descriptif(self):
        return self.__descriptif
    @descriptif.setter
    def descriptif(self, descriptif: str):
        self.__descriptif = descriptif

    @property
    def label(self):
        return self.__label
    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def url(self):
        return self.__url
    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def id_document(self):
        return self.__id_document
    @id_document.setter
    def id_document(self, id_document: int):
        self.__id_document = id_document

    @property
    def session20(self):
        return self.__session20
    @session20.setter
    def session20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Document__session20", None)
        self.__session20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "document21"):
                    opp_val = getattr(item, "document21", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "document21"):
                    opp_val = getattr(item, "document21", None)
                    
                    if opp_val is None:
                        setattr(item, "document21", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Formation:

    def __init__(self, id_formation: int, label: str, descriptif: str, session16: set["Session"] = None, cCP18: set["CCP"] = None):
        self.id_formation = id_formation
        self.label = label
        self.descriptif = descriptif
        self.session16 = session16 if session16 is not None else set()
        self.cCP18 = cCP18 if cCP18 is not None else set()
        
        pass
    @property
    def descriptif(self):
        return self.__descriptif
    @descriptif.setter
    def descriptif(self, descriptif: str):
        self.__descriptif = descriptif

    @property
    def id_formation(self):
        return self.__id_formation
    @id_formation.setter
    def id_formation(self, id_formation: int):
        self.__id_formation = id_formation

    @property
    def label(self):
        return self.__label
    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def cCP18(self):
        return self.__cCP18
    @cCP18.setter
    def cCP18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Formation__cCP18", None)
        self.__cCP18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "formation19"):
                    opp_val = getattr(item, "formation19", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "formation19"):
                    opp_val = getattr(item, "formation19", None)
                    
                    if opp_val is None:
                        setattr(item, "formation19", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def session16(self):
        return self.__session16
    @session16.setter
    def session16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Formation__session16", None)
        self.__session16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "formation17"):
                    opp_val = getattr(item, "formation17", None)
                    
                    if opp_val == self:
                        setattr(item, "formation17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "formation17"):
                    opp_val = getattr(item, "formation17", None)
                    
                    setattr(item, "formation17", self)
                    



class Session:

    def __init__(self, id_session: int, label: str, adresse: str, date_debut: date, date_fin: date, formateur14: set["Formateur"] = None, formation17: "Formation" = None, document21: set["Document"] = None, etudiant23: set["Etudiant"] = None):
        self.id_session = id_session
        self.label = label
        self.adresse = adresse
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.formateur14 = formateur14 if formateur14 is not None else set()
        self.formation17 = formation17
        self.document21 = document21 if document21 is not None else set()
        self.etudiant23 = etudiant23 if etudiant23 is not None else set()
        
        pass
    @property
    def date_fin(self):
        return self.__date_fin
    @date_fin.setter
    def date_fin(self, date_fin: date):
        self.__date_fin = date_fin

    @property
    def label(self):
        return self.__label
    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def adresse(self):
        return self.__adresse
    @adresse.setter
    def adresse(self, adresse: str):
        self.__adresse = adresse

    @property
    def date_debut(self):
        return self.__date_debut
    @date_debut.setter
    def date_debut(self, date_debut: date):
        self.__date_debut = date_debut

    @property
    def id_session(self):
        return self.__id_session
    @id_session.setter
    def id_session(self, id_session: int):
        self.__id_session = id_session

    @property
    def formateur14(self):
        return self.__formateur14
    @formateur14.setter
    def formateur14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Session__formateur14", None)
        self.__formateur14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "session15"):
                    opp_val = getattr(item, "session15", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "session15"):
                    opp_val = getattr(item, "session15", None)
                    
                    if opp_val is None:
                        setattr(item, "session15", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def formation17(self):
        return self.__formation17
    @formation17.setter
    def formation17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Session__formation17", None)
        self.__formation17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "session16"):
                opp_val = getattr(old_value, "session16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "session16"):
                opp_val = getattr(value, "session16", None)
                if opp_val is None:
                    setattr(value, "session16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def etudiant23(self):
        return self.__etudiant23
    @etudiant23.setter
    def etudiant23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Session__etudiant23", None)
        self.__etudiant23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "session22"):
                    opp_val = getattr(item, "session22", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "session22"):
                    opp_val = getattr(item, "session22", None)
                    
                    if opp_val is None:
                        setattr(item, "session22", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def document21(self):
        return self.__document21
    @document21.setter
    def document21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Session__document21", None)
        self.__document21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "session20"):
                    opp_val = getattr(item, "session20", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "session20"):
                    opp_val = getattr(item, "session20", None)
                    
                    if opp_val is None:
                        setattr(item, "session20", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Administrateur:

    def __init__(self, id_administrateur: int, actif: bool, personne13: set["Personne"] = None):
        self.id_administrateur = id_administrateur
        self.actif = actif
        self.personne13 = personne13 if personne13 is not None else set()
        
        pass
    @property
    def actif(self):
        return self.__actif
    @actif.setter
    def actif(self, actif: bool):
        self.__actif = actif

    @property
    def id_administrateur(self):
        return self.__id_administrateur
    @id_administrateur.setter
    def id_administrateur(self, id_administrateur: int):
        self.__id_administrateur = id_administrateur

    @property
    def personne13(self):
        return self.__personne13
    @personne13.setter
    def personne13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrateur__personne13", None)
        self.__personne13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "administrateur12"):
                    opp_val = getattr(item, "administrateur12", None)
                    
                    if opp_val == self:
                        setattr(item, "administrateur12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "administrateur12"):
                    opp_val = getattr(item, "administrateur12", None)
                    
                    setattr(item, "administrateur12", self)
                    



class Direction:

    def __init__(self, id_direction: int, actif: bool, personne11: set["Personne"] = None):
        self.id_direction = id_direction
        self.actif = actif
        self.personne11 = personne11 if personne11 is not None else set()
        
        pass
    @property
    def actif(self):
        return self.__actif
    @actif.setter
    def actif(self, actif: bool):
        self.__actif = actif

    @property
    def id_direction(self):
        return self.__id_direction
    @id_direction.setter
    def id_direction(self, id_direction: int):
        self.__id_direction = id_direction

    @property
    def personne11(self):
        return self.__personne11
    @personne11.setter
    def personne11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Direction__personne11", None)
        self.__personne11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "direction10"):
                    opp_val = getattr(item, "direction10", None)
                    
                    if opp_val == self:
                        setattr(item, "direction10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "direction10"):
                    opp_val = getattr(item, "direction10", None)
                    
                    setattr(item, "direction10", self)
                    



class Formateur:

    def __init__(self, id_formateur: int, actif: bool, personne9: set["Personne"] = None, session15: set["Session"] = None):
        self.id_formateur = id_formateur
        self.actif = actif
        self.personne9 = personne9 if personne9 is not None else set()
        self.session15 = session15 if session15 is not None else set()
        
        pass
    @property
    def id_formateur(self):
        return self.__id_formateur
    @id_formateur.setter
    def id_formateur(self, id_formateur: int):
        self.__id_formateur = id_formateur

    @property
    def actif(self):
        return self.__actif
    @actif.setter
    def actif(self, actif: bool):
        self.__actif = actif

    @property
    def personne9(self):
        return self.__personne9
    @personne9.setter
    def personne9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Formateur__personne9", None)
        self.__personne9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "formateur8"):
                    opp_val = getattr(item, "formateur8", None)
                    
                    if opp_val == self:
                        setattr(item, "formateur8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "formateur8"):
                    opp_val = getattr(item, "formateur8", None)
                    
                    setattr(item, "formateur8", self)
                    

    @property
    def session15(self):
        return self.__session15
    @session15.setter
    def session15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Formateur__session15", None)
        self.__session15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "formateur14"):
                    opp_val = getattr(item, "formateur14", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "formateur14"):
                    opp_val = getattr(item, "formateur14", None)
                    
                    if opp_val is None:
                        setattr(item, "formateur14", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Etudiant:

    def __init__(self, id_etudiant: int, list_notes: float, list_commentaire: str, cv: str, actif: bool, personne7: set["Personne"] = None, session22: set["Session"] = None):
        self.id_etudiant = id_etudiant
        self.list_notes = list_notes
        self.list_commentaire = list_commentaire
        self.cv = cv
        self.actif = actif
        self.personne7 = personne7 if personne7 is not None else set()
        self.session22 = session22 if session22 is not None else set()
        
        pass
    @property
    def list_notes(self):
        return self.__list_notes
    @list_notes.setter
    def list_notes(self, list_notes: float):
        self.__list_notes = list_notes

    @property
    def list_commentaire(self):
        return self.__list_commentaire
    @list_commentaire.setter
    def list_commentaire(self, list_commentaire: str):
        self.__list_commentaire = list_commentaire

    @property
    def cv(self):
        return self.__cv
    @cv.setter
    def cv(self, cv: str):
        self.__cv = cv

    @property
    def actif(self):
        return self.__actif
    @actif.setter
    def actif(self, actif: bool):
        self.__actif = actif

    @property
    def id_etudiant(self):
        return self.__id_etudiant
    @id_etudiant.setter
    def id_etudiant(self, id_etudiant: int):
        self.__id_etudiant = id_etudiant

    @property
    def session22(self):
        return self.__session22
    @session22.setter
    def session22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etudiant__session22", None)
        self.__session22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etudiant23"):
                    opp_val = getattr(item, "etudiant23", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etudiant23"):
                    opp_val = getattr(item, "etudiant23", None)
                    
                    if opp_val is None:
                        setattr(item, "etudiant23", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def personne7(self):
        return self.__personne7
    @personne7.setter
    def personne7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etudiant__personne7", None)
        self.__personne7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etudiant6"):
                    opp_val = getattr(item, "etudiant6", None)
                    
                    if opp_val == self:
                        setattr(item, "etudiant6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etudiant6"):
                    opp_val = getattr(item, "etudiant6", None)
                    
                    setattr(item, "etudiant6", self)
                    



class Personne:

    def __init__(self, id: int, nom: str, prenom: str, naissance: date, telephone: str, mail: str, photo: str, etudiant6: "Etudiant" = None, formateur8: "Formateur" = None, direction10: "Direction" = None, administrateur12: "Administrateur" = None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.naissance = naissance
        self.telephone = telephone
        self.mail = mail
        self.photo = photo
        self.etudiant6 = etudiant6
        self.formateur8 = formateur8
        self.direction10 = direction10
        self.administrateur12 = administrateur12
        
        pass
    @property
    def photo(self):
        return self.__photo
    @photo.setter
    def photo(self, photo: str):
        self.__photo = photo

    @property
    def mail(self):
        return self.__mail
    @mail.setter
    def mail(self, mail: str):
        self.__mail = mail

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def telephone(self):
        return self.__telephone
    @telephone.setter
    def telephone(self, telephone: str):
        self.__telephone = telephone

    @property
    def naissance(self):
        return self.__naissance
    @naissance.setter
    def naissance(self, naissance: date):
        self.__naissance = naissance

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, prenom: str):
        self.__prenom = prenom

    @property
    def administrateur12(self):
        return self.__administrateur12
    @administrateur12.setter
    def administrateur12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personne__administrateur12", None)
        self.__administrateur12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personne13"):
                opp_val = getattr(old_value, "personne13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personne13"):
                opp_val = getattr(value, "personne13", None)
                if opp_val is None:
                    setattr(value, "personne13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def direction10(self):
        return self.__direction10
    @direction10.setter
    def direction10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personne__direction10", None)
        self.__direction10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personne11"):
                opp_val = getattr(old_value, "personne11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personne11"):
                opp_val = getattr(value, "personne11", None)
                if opp_val is None:
                    setattr(value, "personne11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def etudiant6(self):
        return self.__etudiant6
    @etudiant6.setter
    def etudiant6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personne__etudiant6", None)
        self.__etudiant6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personne7"):
                opp_val = getattr(old_value, "personne7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personne7"):
                opp_val = getattr(value, "personne7", None)
                if opp_val is None:
                    setattr(value, "personne7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def formateur8(self):
        return self.__formateur8
    @formateur8.setter
    def formateur8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personne__formateur8", None)
        self.__formateur8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personne9"):
                opp_val = getattr(old_value, "personne9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personne9"):
                opp_val = getattr(value, "personne9", None)
                if opp_val is None:
                    setattr(value, "personne9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



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


class ClassN:

    pass


class ClassM:

    pass


class ClassL:

    pass


class ClassK:

    pass


class ClassH:

    pass


class ClassJ:

    pass


class ClassG:

    pass


class ClassF:

    pass


class ClassE:

    pass


class ClassD:

    pass


class ClassC:

    def __init__(self, publicAttribute: float, privateAttribute: int, protectedAttribute: str, packageAttribute: str):
        self.publicAttribute = publicAttribute
        self.privateAttribute = privateAttribute
        self.protectedAttribute = protectedAttribute
        self.packageAttribute = packageAttribute
        
        pass
    @property
    def publicAttribute(self):
        return self.__publicAttribute
    @publicAttribute.setter
    def publicAttribute(self, publicAttribute: float):
        self.__publicAttribute = publicAttribute

    @property
    def protectedAttribute(self):
        return self.__protectedAttribute
    @protectedAttribute.setter
    def protectedAttribute(self, protectedAttribute: str):
        self.__protectedAttribute = protectedAttribute

    @property
    def packageAttribute(self):
        return self.__packageAttribute
    @packageAttribute.setter
    def packageAttribute(self, packageAttribute: str):
        self.__packageAttribute = packageAttribute

    @property
    def privateAttribute(self):
        return self.__privateAttribute
    @privateAttribute.setter
    def privateAttribute(self, privateAttribute: int):
        self.__privateAttribute = privateAttribute



class ClassB:

    pass


class ClassA:

    def __init__(self, publicAttribute: float, privateAttribute: int, protectedAttribute: str, packageAttribute: str):
        self.publicAttribute = publicAttribute
        self.privateAttribute = privateAttribute
        self.protectedAttribute = protectedAttribute
        self.packageAttribute = packageAttribute
        
        pass
    @property
    def privateAttribute(self):
        return self.__privateAttribute
    @privateAttribute.setter
    def privateAttribute(self, privateAttribute: int):
        self.__privateAttribute = privateAttribute

    @property
    def publicAttribute(self):
        return self.__publicAttribute
    @publicAttribute.setter
    def publicAttribute(self, publicAttribute: float):
        self.__publicAttribute = publicAttribute

    @property
    def packageAttribute(self):
        return self.__packageAttribute
    @packageAttribute.setter
    def packageAttribute(self, packageAttribute: str):
        self.__packageAttribute = packageAttribute

    @property
    def protectedAttribute(self):
        return self.__protectedAttribute
    @protectedAttribute.setter
    def protectedAttribute(self, protectedAttribute: str):
        self.__protectedAttribute = protectedAttribute



class BankAccount:

    def __init__(self, ownerName: str, balance: float):
        self.ownerName = ownerName
        self.balance = balance
        
        pass
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

    @property
    def ownerName(self):
        return self.__ownerName
    @ownerName.setter
    def ownerName(self, ownerName: str):
        self.__ownerName = ownerName

