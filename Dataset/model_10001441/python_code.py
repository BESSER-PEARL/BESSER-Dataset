from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class IHM(Enum):
    pass
class Information(Enum):
    pass

############################################
# Definition of Classes
############################################







class Controlleur_Actor:

    pass





class Pr_sentation:

    def __init__(self, numTel: str, siteDeCommande: str, ouverture: str, description: str, adresse: str, repr_sente16: "FicheRestaurant" = None):
        self.numTel = numTel
        self.siteDeCommande = siteDeCommande
        self.ouverture = ouverture
        self.description = description
        self.adresse = adresse
        self.repr_sente16 = repr_sente16
        
        pass
    @property
    def numTel(self):
        return self.__numTel
    @numTel.setter
    def numTel(self, numTel: str):
        self.__numTel = numTel

    @property
    def ouverture(self):
        return self.__ouverture
    @ouverture.setter
    def ouverture(self, ouverture: str):
        self.__ouverture = ouverture

    @property
    def siteDeCommande(self):
        return self.__siteDeCommande
    @siteDeCommande.setter
    def siteDeCommande(self, siteDeCommande: str):
        self.__siteDeCommande = siteDeCommande

    @property
    def adresse(self):
        return self.__adresse
    @adresse.setter
    def adresse(self, adresse: str):
        self.__adresse = adresse

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def repr_sente16(self):
        return self.__repr_sente16
    @repr_sente16.setter
    def repr_sente16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pr_sentation__repr_sente16", None)
        self.__repr_sente16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "poss_de17"):
                opp_val = getattr(old_value, "poss_de17", None)
                if opp_val == self:
                    setattr(old_value, "poss_de17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "poss_de17"):
                opp_val = getattr(value, "poss_de17", None)
                setattr(value, "poss_de17", self)



class Photo:

    pass


class Commentaire:

    def __init__(self, auteur: Analyse_Compte, commentaire: str, avisGlobal10: "AvisGlobal" = None):
        self.auteur = auteur
        self.commentaire = commentaire
        self.avisGlobal10 = avisGlobal10
        
        pass
    @property
    def auteur(self):
        return self.__auteur
    @auteur.setter
    def auteur(self, auteur: Analyse_Compte):
        self.__auteur = auteur

    @property
    def commentaire(self):
        return self.__commentaire
    @commentaire.setter
    def commentaire(self, commentaire: str):
        self.__commentaire = commentaire

    @property
    def avisGlobal10(self):
        return self.__avisGlobal10
    @avisGlobal10.setter
    def avisGlobal10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Commentaire__avisGlobal10", None)
        self.__avisGlobal10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commentaire11"):
                opp_val = getattr(old_value, "commentaire11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commentaire11"):
                opp_val = getattr(value, "commentaire11", None)
                if opp_val is None:
                    setattr(value, "commentaire11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class AvisGlobal:

    def __init__(self, note: str, nbAvis: int, diagramme: str, Commentaires: str, commentaire11: set["Commentaire"] = None, d_finit12: "FicheRestaurant" = None):
        self.note = note
        self.nbAvis = nbAvis
        self.diagramme = diagramme
        self.Commentaires = Commentaires
        self.commentaire11 = commentaire11 if commentaire11 is not None else set()
        self.d_finit12 = d_finit12
        
        pass
    @property
    def nbAvis(self):
        return self.__nbAvis
    @nbAvis.setter
    def nbAvis(self, nbAvis: int):
        self.__nbAvis = nbAvis

    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def diagramme(self):
        return self.__diagramme
    @diagramme.setter
    def diagramme(self, diagramme: str):
        self.__diagramme = diagramme

    @property
    def Commentaires(self):
        return self.__Commentaires
    @Commentaires.setter
    def Commentaires(self, Commentaires: str):
        self.__Commentaires = Commentaires

    @property
    def d_finit12(self):
        return self.__d_finit12
    @d_finit12.setter
    def d_finit12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AvisGlobal__d_finit12", None)
        self.__d_finit12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "poss_de13"):
                opp_val = getattr(old_value, "poss_de13", None)
                if opp_val == self:
                    setattr(old_value, "poss_de13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "poss_de13"):
                opp_val = getattr(value, "poss_de13", None)
                setattr(value, "poss_de13", self)

    @property
    def commentaire11(self):
        return self.__commentaire11
    @commentaire11.setter
    def commentaire11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AvisGlobal__commentaire11", None)
        self.__commentaire11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avisGlobal10"):
                    opp_val = getattr(item, "avisGlobal10", None)
                    
                    if opp_val == self:
                        setattr(item, "avisGlobal10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avisGlobal10"):
                    opp_val = getattr(item, "avisGlobal10", None)
                    
                    setattr(item, "avisGlobal10", self)
                    



class FicheRestaurant:

    def __init__(self, nom: str, poss_de13: "AvisGlobal" = None, poss_de14: set["Photo"] = None, poss_de17: "Pr_sentation" = None):
        self.nom = nom
        self.poss_de13 = poss_de13
        self.poss_de14 = poss_de14 if poss_de14 is not None else set()
        self.poss_de17 = poss_de17
        
        pass
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def poss_de14(self):
        return self.__poss_de14
    @poss_de14.setter
    def poss_de14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FicheRestaurant__poss_de14", None)
        self.__poss_de14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repr_sente15"):
                    opp_val = getattr(item, "repr_sente15", None)
                    
                    if opp_val == self:
                        setattr(item, "repr_sente15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repr_sente15"):
                    opp_val = getattr(item, "repr_sente15", None)
                    
                    setattr(item, "repr_sente15", self)
                    

    @property
    def poss_de17(self):
        return self.__poss_de17
    @poss_de17.setter
    def poss_de17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FicheRestaurant__poss_de17", None)
        self.__poss_de17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repr_sente16"):
                opp_val = getattr(old_value, "repr_sente16", None)
                if opp_val == self:
                    setattr(old_value, "repr_sente16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repr_sente16"):
                opp_val = getattr(value, "repr_sente16", None)
                setattr(value, "repr_sente16", self)

    @property
    def poss_de13(self):
        return self.__poss_de13
    @poss_de13.setter
    def poss_de13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FicheRestaurant__poss_de13", None)
        self.__poss_de13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "d_finit12"):
                opp_val = getattr(old_value, "d_finit12", None)
                if opp_val == self:
                    setattr(old_value, "d_finit12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "d_finit12"):
                opp_val = getattr(value, "d_finit12", None)
                setattr(value, "d_finit12", self)



class Analyse_Moderateurs:

    pass


class Analyse_Criteres:

    def __init__(self, rapportQualitePrix: int, rapidite: int, qualit_: int, respectHoraires: int, amabilite: int, sont_associ_s6: set["Analyse_Review"] = None):
        self.rapportQualitePrix = rapportQualitePrix
        self.rapidite = rapidite
        self.qualit_ = qualit_
        self.respectHoraires = respectHoraires
        self.amabilite = amabilite
        self.sont_associ_s6 = sont_associ_s6 if sont_associ_s6 is not None else set()
        
        pass
    @property
    def respectHoraires(self):
        return self.__respectHoraires
    @respectHoraires.setter
    def respectHoraires(self, respectHoraires: int):
        self.__respectHoraires = respectHoraires

    @property
    def rapidite(self):
        return self.__rapidite
    @rapidite.setter
    def rapidite(self, rapidite: int):
        self.__rapidite = rapidite

    @property
    def amabilite(self):
        return self.__amabilite
    @amabilite.setter
    def amabilite(self, amabilite: int):
        self.__amabilite = amabilite

    @property
    def rapportQualitePrix(self):
        return self.__rapportQualitePrix
    @rapportQualitePrix.setter
    def rapportQualitePrix(self, rapportQualitePrix: int):
        self.__rapportQualitePrix = rapportQualitePrix

    @property
    def qualit_(self):
        return self.__qualit_
    @qualit_.setter
    def qualit_(self, qualit_: int):
        self.__qualit_ = qualit_

    @property
    def sont_associ_s6(self):
        return self.__sont_associ_s6
    @sont_associ_s6.setter
    def sont_associ_s6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse_Criteres__sont_associ_s6", None)
        self.__sont_associ_s6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "note7"):
                    opp_val = getattr(item, "note7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "note7"):
                    opp_val = getattr(item, "note7", None)
                    
                    if opp_val is None:
                        setattr(item, "note7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Analyse_Compte:

    def __init__(self, login: str, motdepasse: str, est_associ_2: "Analyse_Utilisateur" = None, poss_de4: set["Analyse_Review"] = None, est_associ_9: "Analyse_Moderateurs" = None):
        self.login = login
        self.motdepasse = motdepasse
        self.est_associ_2 = est_associ_2
        self.poss_de4 = poss_de4 if poss_de4 is not None else set()
        self.est_associ_9 = est_associ_9
        
        pass
    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def motdepasse(self):
        return self.__motdepasse
    @motdepasse.setter
    def motdepasse(self, motdepasse: str):
        self.__motdepasse = motdepasse

    @property
    def est_associ_2(self):
        return self.__est_associ_2
    @est_associ_2.setter
    def est_associ_2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse_Compte__est_associ_2", None)
        self.__est_associ_2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "poss_de3"):
                opp_val = getattr(old_value, "poss_de3", None)
                if opp_val == self:
                    setattr(old_value, "poss_de3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "poss_de3"):
                opp_val = getattr(value, "poss_de3", None)
                setattr(value, "poss_de3", self)

    @property
    def est_associ_9(self):
        return self.__est_associ_9
    @est_associ_9.setter
    def est_associ_9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse_Compte__est_associ_9", None)
        self.__est_associ_9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "poss_de8"):
                opp_val = getattr(old_value, "poss_de8", None)
                if opp_val == self:
                    setattr(old_value, "poss_de8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "poss_de8"):
                opp_val = getattr(value, "poss_de8", None)
                setattr(value, "poss_de8", self)

    @property
    def poss_de4(self):
        return self.__poss_de4
    @poss_de4.setter
    def poss_de4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse_Compte__poss_de4", None)
        self.__poss_de4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "est__crite5"):
                    opp_val = getattr(item, "est__crite5", None)
                    
                    if opp_val == self:
                        setattr(item, "est__crite5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "est__crite5"):
                    opp_val = getattr(item, "est__crite5", None)
                    
                    setattr(item, "est__crite5", self)
                    



class Analyse_Utilisateur:

    pass


class Analyse_Review:

    def __init__(self, NoteGlobale: int, lesNotes: str, Commentaire: str, caract_rise0: "Analyse_Fast_Food" = None, est__crite5: "Analyse_Compte" = None, note7: set["Analyse_Criteres"] = None):
        self.NoteGlobale = NoteGlobale
        self.lesNotes = lesNotes
        self.Commentaire = Commentaire
        self.caract_rise0 = caract_rise0
        self.est__crite5 = est__crite5
        self.note7 = note7 if note7 is not None else set()
        
        pass
    @property
    def Commentaire(self):
        return self.__Commentaire
    @Commentaire.setter
    def Commentaire(self, Commentaire: str):
        self.__Commentaire = Commentaire

    @property
    def NoteGlobale(self):
        return self.__NoteGlobale
    @NoteGlobale.setter
    def NoteGlobale(self, NoteGlobale: int):
        self.__NoteGlobale = NoteGlobale

    @property
    def lesNotes(self):
        return self.__lesNotes
    @lesNotes.setter
    def lesNotes(self, lesNotes: str):
        self.__lesNotes = lesNotes

    @property
    def caract_rise0(self):
        return self.__caract_rise0
    @caract_rise0.setter
    def caract_rise0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse_Review__caract_rise0", None)
        self.__caract_rise0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "poss_de1"):
                opp_val = getattr(old_value, "poss_de1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "poss_de1"):
                opp_val = getattr(value, "poss_de1", None)
                if opp_val is None:
                    setattr(value, "poss_de1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def est__crite5(self):
        return self.__est__crite5
    @est__crite5.setter
    def est__crite5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse_Review__est__crite5", None)
        self.__est__crite5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "poss_de4"):
                opp_val = getattr(old_value, "poss_de4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "poss_de4"):
                opp_val = getattr(value, "poss_de4", None)
                if opp_val is None:
                    setattr(value, "poss_de4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def note7(self):
        return self.__note7
    @note7.setter
    def note7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse_Review__note7", None)
        self.__note7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sont_associ_s6"):
                    opp_val = getattr(item, "sont_associ_s6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sont_associ_s6"):
                    opp_val = getattr(item, "sont_associ_s6", None)
                    
                    if opp_val is None:
                        setattr(item, "sont_associ_s6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Analyse_Fast_Food:

    def __init__(self, Adresse: str, Ville: str, nbPlaces: int, nom: str, prixMax: int, prixMin: int, numeroTel: str, horaires: str, proprietaire: str, notes: str, photos: str, poss_de1: set["Analyse_Review"] = None):
        self.Adresse = Adresse
        self.Ville = Ville
        self.nbPlaces = nbPlaces
        self.nom = nom
        self.prixMax = prixMax
        self.prixMin = prixMin
        self.numeroTel = numeroTel
        self.horaires = horaires
        self.proprietaire = proprietaire
        self.notes = notes
        self.photos = photos
        self.poss_de1 = poss_de1 if poss_de1 is not None else set()
        
        pass
    @property
    def horaires(self):
        return self.__horaires
    @horaires.setter
    def horaires(self, horaires: str):
        self.__horaires = horaires

    @property
    def Ville(self):
        return self.__Ville
    @Ville.setter
    def Ville(self, Ville: str):
        self.__Ville = Ville

    @property
    def prixMax(self):
        return self.__prixMax
    @prixMax.setter
    def prixMax(self, prixMax: int):
        self.__prixMax = prixMax

    @property
    def numeroTel(self):
        return self.__numeroTel
    @numeroTel.setter
    def numeroTel(self, numeroTel: str):
        self.__numeroTel = numeroTel

    @property
    def proprietaire(self):
        return self.__proprietaire
    @proprietaire.setter
    def proprietaire(self, proprietaire: str):
        self.__proprietaire = proprietaire

    @property
    def nbPlaces(self):
        return self.__nbPlaces
    @nbPlaces.setter
    def nbPlaces(self, nbPlaces: int):
        self.__nbPlaces = nbPlaces

    @property
    def photos(self):
        return self.__photos
    @photos.setter
    def photos(self, photos: str):
        self.__photos = photos

    @property
    def notes(self):
        return self.__notes
    @notes.setter
    def notes(self, notes: str):
        self.__notes = notes

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def prixMin(self):
        return self.__prixMin
    @prixMin.setter
    def prixMin(self, prixMin: int):
        self.__prixMin = prixMin

    @property
    def Adresse(self):
        return self.__Adresse
    @Adresse.setter
    def Adresse(self, Adresse: str):
        self.__Adresse = Adresse

    @property
    def poss_de1(self):
        return self.__poss_de1
    @poss_de1.setter
    def poss_de1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse_Fast_Food__poss_de1", None)
        self.__poss_de1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caract_rise0"):
                    opp_val = getattr(item, "caract_rise0", None)
                    
                    if opp_val == self:
                        setattr(item, "caract_rise0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caract_rise0"):
                    opp_val = getattr(item, "caract_rise0", None)
                    
                    setattr(item, "caract_rise0", self)
                    



class Analyse2_AvisGlobal:

    def __init__(self, notes: str, nbAvis: int, Commentaires: str, fast_Food28: "Analyse2_Fast_Food" = None):
        self.notes = notes
        self.nbAvis = nbAvis
        self.Commentaires = Commentaires
        self.fast_Food28 = fast_Food28
        
        pass
    @property
    def nbAvis(self):
        return self.__nbAvis
    @nbAvis.setter
    def nbAvis(self, nbAvis: int):
        self.__nbAvis = nbAvis

    @property
    def notes(self):
        return self.__notes
    @notes.setter
    def notes(self, notes: str):
        self.__notes = notes

    @property
    def Commentaires(self):
        return self.__Commentaires
    @Commentaires.setter
    def Commentaires(self, Commentaires: str):
        self.__Commentaires = Commentaires

    @property
    def fast_Food28(self):
        return self.__fast_Food28
    @fast_Food28.setter
    def fast_Food28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse2_AvisGlobal__fast_Food28", None)
        self.__fast_Food28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avisGlobal29"):
                opp_val = getattr(old_value, "avisGlobal29", None)
                if opp_val == self:
                    setattr(old_value, "avisGlobal29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avisGlobal29"):
                opp_val = getattr(value, "avisGlobal29", None)
                setattr(value, "avisGlobal29", self)



class Analyse2_Moderateurs:

    pass


class Analyse2_Criteres:

    def __init__(self, rapportQualitePrix: int, rapidite: int, qualit_: int, respectHoraires: int, amabilite: int, sont_associ_s24: set["Analyse2_Review"] = None):
        self.rapportQualitePrix = rapportQualitePrix
        self.rapidite = rapidite
        self.qualit_ = qualit_
        self.respectHoraires = respectHoraires
        self.amabilite = amabilite
        self.sont_associ_s24 = sont_associ_s24 if sont_associ_s24 is not None else set()
        
        pass
    @property
    def respectHoraires(self):
        return self.__respectHoraires
    @respectHoraires.setter
    def respectHoraires(self, respectHoraires: int):
        self.__respectHoraires = respectHoraires

    @property
    def qualit_(self):
        return self.__qualit_
    @qualit_.setter
    def qualit_(self, qualit_: int):
        self.__qualit_ = qualit_

    @property
    def rapportQualitePrix(self):
        return self.__rapportQualitePrix
    @rapportQualitePrix.setter
    def rapportQualitePrix(self, rapportQualitePrix: int):
        self.__rapportQualitePrix = rapportQualitePrix

    @property
    def amabilite(self):
        return self.__amabilite
    @amabilite.setter
    def amabilite(self, amabilite: int):
        self.__amabilite = amabilite

    @property
    def rapidite(self):
        return self.__rapidite
    @rapidite.setter
    def rapidite(self, rapidite: int):
        self.__rapidite = rapidite

    @property
    def sont_associ_s24(self):
        return self.__sont_associ_s24
    @sont_associ_s24.setter
    def sont_associ_s24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse2_Criteres__sont_associ_s24", None)
        self.__sont_associ_s24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "note25"):
                    opp_val = getattr(item, "note25", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "note25"):
                    opp_val = getattr(item, "note25", None)
                    
                    if opp_val is None:
                        setattr(item, "note25", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Analyse2_Compte:

    def __init__(self, login: str, motdepasse: str, est_associ_20: "Analyse2_Utilisateur" = None, poss_de22: set["Analyse2_Review"] = None, est_associ_27: "Analyse2_Moderateurs" = None):
        self.login = login
        self.motdepasse = motdepasse
        self.est_associ_20 = est_associ_20
        self.poss_de22 = poss_de22 if poss_de22 is not None else set()
        self.est_associ_27 = est_associ_27
        
        pass
    @property
    def motdepasse(self):
        return self.__motdepasse
    @motdepasse.setter
    def motdepasse(self, motdepasse: str):
        self.__motdepasse = motdepasse

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def est_associ_27(self):
        return self.__est_associ_27
    @est_associ_27.setter
    def est_associ_27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse2_Compte__est_associ_27", None)
        self.__est_associ_27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "poss_de26"):
                opp_val = getattr(old_value, "poss_de26", None)
                if opp_val == self:
                    setattr(old_value, "poss_de26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "poss_de26"):
                opp_val = getattr(value, "poss_de26", None)
                setattr(value, "poss_de26", self)

    @property
    def poss_de22(self):
        return self.__poss_de22
    @poss_de22.setter
    def poss_de22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse2_Compte__poss_de22", None)
        self.__poss_de22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "est__crite23"):
                    opp_val = getattr(item, "est__crite23", None)
                    
                    if opp_val == self:
                        setattr(item, "est__crite23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "est__crite23"):
                    opp_val = getattr(item, "est__crite23", None)
                    
                    setattr(item, "est__crite23", self)
                    

    @property
    def est_associ_20(self):
        return self.__est_associ_20
    @est_associ_20.setter
    def est_associ_20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse2_Compte__est_associ_20", None)
        self.__est_associ_20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "poss_de21"):
                opp_val = getattr(old_value, "poss_de21", None)
                if opp_val == self:
                    setattr(old_value, "poss_de21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "poss_de21"):
                opp_val = getattr(value, "poss_de21", None)
                setattr(value, "poss_de21", self)



class Analyse2_Utilisateur:

    pass


class Analyse2_Review:

    def __init__(self, utilite: str, lesNotes: str, Commentaire: str, caract_rise18: "Analyse2_Fast_Food" = None, est__crite23: "Analyse2_Compte" = None, note25: set["Analyse2_Criteres"] = None):
        self.utilite = utilite
        self.lesNotes = lesNotes
        self.Commentaire = Commentaire
        self.caract_rise18 = caract_rise18
        self.est__crite23 = est__crite23
        self.note25 = note25 if note25 is not None else set()
        
        pass
    @property
    def lesNotes(self):
        return self.__lesNotes
    @lesNotes.setter
    def lesNotes(self, lesNotes: str):
        self.__lesNotes = lesNotes

    @property
    def Commentaire(self):
        return self.__Commentaire
    @Commentaire.setter
    def Commentaire(self, Commentaire: str):
        self.__Commentaire = Commentaire

    @property
    def utilite(self):
        return self.__utilite
    @utilite.setter
    def utilite(self, utilite: str):
        self.__utilite = utilite

    @property
    def est__crite23(self):
        return self.__est__crite23
    @est__crite23.setter
    def est__crite23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse2_Review__est__crite23", None)
        self.__est__crite23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "poss_de22"):
                opp_val = getattr(old_value, "poss_de22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "poss_de22"):
                opp_val = getattr(value, "poss_de22", None)
                if opp_val is None:
                    setattr(value, "poss_de22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def caract_rise18(self):
        return self.__caract_rise18
    @caract_rise18.setter
    def caract_rise18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse2_Review__caract_rise18", None)
        self.__caract_rise18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "poss_de19"):
                opp_val = getattr(old_value, "poss_de19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "poss_de19"):
                opp_val = getattr(value, "poss_de19", None)
                if opp_val is None:
                    setattr(value, "poss_de19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def note25(self):
        return self.__note25
    @note25.setter
    def note25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse2_Review__note25", None)
        self.__note25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sont_associ_s24"):
                    opp_val = getattr(item, "sont_associ_s24", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sont_associ_s24"):
                    opp_val = getattr(item, "sont_associ_s24", None)
                    
                    if opp_val is None:
                        setattr(item, "sont_associ_s24", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Analyse2_Fast_Food:

    def __init__(self, nom: str, numeroTel: str, siteDeCommande: str, description: str, horaires: str, Adresse: str, Ville: str, nbPlaces: int, prixMax: int, prixMin: int, proprietaire: str, reviews: str, photos: str, poss_de19: set["Analyse2_Review"] = None, avisGlobal29: "Analyse2_AvisGlobal" = None):
        self.nom = nom
        self.numeroTel = numeroTel
        self.siteDeCommande = siteDeCommande
        self.description = description
        self.horaires = horaires
        self.Adresse = Adresse
        self.Ville = Ville
        self.nbPlaces = nbPlaces
        self.prixMax = prixMax
        self.prixMin = prixMin
        self.proprietaire = proprietaire
        self.reviews = reviews
        self.photos = photos
        self.poss_de19 = poss_de19 if poss_de19 is not None else set()
        self.avisGlobal29 = avisGlobal29
        
        pass
    @property
    def photos(self):
        return self.__photos
    @photos.setter
    def photos(self, photos: str):
        self.__photos = photos

    @property
    def Adresse(self):
        return self.__Adresse
    @Adresse.setter
    def Adresse(self, Adresse: str):
        self.__Adresse = Adresse

    @property
    def proprietaire(self):
        return self.__proprietaire
    @proprietaire.setter
    def proprietaire(self, proprietaire: str):
        self.__proprietaire = proprietaire

    @property
    def prixMax(self):
        return self.__prixMax
    @prixMax.setter
    def prixMax(self, prixMax: int):
        self.__prixMax = prixMax

    @property
    def siteDeCommande(self):
        return self.__siteDeCommande
    @siteDeCommande.setter
    def siteDeCommande(self, siteDeCommande: str):
        self.__siteDeCommande = siteDeCommande

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def nbPlaces(self):
        return self.__nbPlaces
    @nbPlaces.setter
    def nbPlaces(self, nbPlaces: int):
        self.__nbPlaces = nbPlaces

    @property
    def prixMin(self):
        return self.__prixMin
    @prixMin.setter
    def prixMin(self, prixMin: int):
        self.__prixMin = prixMin

    @property
    def reviews(self):
        return self.__reviews
    @reviews.setter
    def reviews(self, reviews: str):
        self.__reviews = reviews

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def Ville(self):
        return self.__Ville
    @Ville.setter
    def Ville(self, Ville: str):
        self.__Ville = Ville

    @property
    def horaires(self):
        return self.__horaires
    @horaires.setter
    def horaires(self, horaires: str):
        self.__horaires = horaires

    @property
    def numeroTel(self):
        return self.__numeroTel
    @numeroTel.setter
    def numeroTel(self, numeroTel: str):
        self.__numeroTel = numeroTel

    @property
    def poss_de19(self):
        return self.__poss_de19
    @poss_de19.setter
    def poss_de19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse2_Fast_Food__poss_de19", None)
        self.__poss_de19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caract_rise18"):
                    opp_val = getattr(item, "caract_rise18", None)
                    
                    if opp_val == self:
                        setattr(item, "caract_rise18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caract_rise18"):
                    opp_val = getattr(item, "caract_rise18", None)
                    
                    setattr(item, "caract_rise18", self)
                    

    @property
    def avisGlobal29(self):
        return self.__avisGlobal29
    @avisGlobal29.setter
    def avisGlobal29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Analyse2_Fast_Food__avisGlobal29", None)
        self.__avisGlobal29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fast_Food28"):
                opp_val = getattr(old_value, "fast_Food28", None)
                if opp_val == self:
                    setattr(old_value, "fast_Food28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fast_Food28"):
                opp_val = getattr(value, "fast_Food28", None)
                setattr(value, "fast_Food28", self)

