from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################







class commande_Payer_commande_UseCase:

    pass


class commande_Creer_commande_UseCase:

    pass


class compte_Gerer_Commande_UseCase:

    pass


class compte_S_authentifier_UseCase:

    pass


class compte_Ajouter_commentaire_UseCase:

    pass


class compte_Gerer_le_compte_UseCase:

    pass


class Systeme_Paiement_Actor:

    pass


class Administrateur_Actor:

    pass


class Visiteur_Actor:

    pass


class Client_Actor:

    pass


class backoffice_Gerer_les_auteurs_UseCase:

    pass


class backoffice_Gerer_les_editeurs_UseCase:

    pass


class backoffice_Valider_les_commentaires_UseCase:

    pass


class backoffice_Gerer_les_categories_UseCase:

    pass


class backoffice_S_authentifier_UseCase:

    pass


class backoffice_Gerer_les_produits_UseCase:

    pass


class navigation_Afficher_la_liste_des_livres_UseCase:

    pass


class navigation_Recherche_par_critere_UseCase:

    pass


class information_Consulter_l_aide_UseCase:

    pass


class panier_Passer_une_commande_UseCase:

    pass


class panier_Modifier_quantite_livre_UseCase:

    pass


class panier_Gerer_panier_UseCase:

    pass


class panier_Supprimer_du_panier_UseCase:

    pass


class panier_Ajouter_au_panier_UseCase:

    pass


class navigation_Rechercher_un_livre_UseCase:

    pass


class navigation_Parcourir_les_livres_UseCase:

    pass


class commande_Annuler_commande_UseCase:

    pass


class commande_Suivre_commande_UseCase:

    pass





class be_jebouquine_dao_EtatCommandeDAO:

    pass


class be_jebouquine_dao_CommandeDAO:

    pass


class be_jebouquine_dao_ClientDAO:

    pass


class be_jebouquine_dao_LigneCommandeDAO:

    pass


class be_jebouquine_dao_CommentaireDAO:

    pass


class be_jebouquine_dao_CategorieDAO:

    pass


class be_jebouquine_dao_LivraisonInfoDAO:

    pass


class be_jebouquine_dao_LivreDAO:

    pass


class be_jebouquine_dao_EditeurDAO:

    pass


class be_jebouquine_dao_LangueDAO:

    pass


class be_jebouquine_dao_AuteurDAO:

    pass


class be_jebouquine_dao_AdministrateurDAO:

    pass


class be_jebouquine_dao_AbstractFactory(ABC):

    pass


class Collection_Object_:

    pass


class Object:

    pass


class Collection_Client_:

    pass


class be_jebouquine_bo_ICategorieBORemote_Interface:

    pass


class be_jebouquine_bo_IEtatCommandeRemote_Interface:

    pass


class be_jebouquine_bo_LigneCommandeBORemote_Interface:

    pass


class be_jebouquine_bo_IAdministrateurBORemote_Interface:

    pass


class be_jebouquine_bo_LivraisonTypeBORemote_Interface:

    pass


class be_jebouquine_bo_IPanierBORemote_Interface:

    pass


class be_jebouquine_bo_IAuteurBORemote_Interface:

    pass


class be_jebouquine_bo_ILivreBORemote_Interface:

    pass


class be_jebouquine_bo_IEditeurBORemote_Interface:

    pass


class be_jebouquine_bo_ICommentaireBORemote_Interface:

    pass


class be_jebouquine_bo_IClientBORemote_Interface:

    pass


class be_jebouquine_bo_ILangueBORemote_Interface:

    pass


class be_jebouquine_bo_ICommandeBORemote_Interface:

    pass


class be_jebouquine_bo_AdministrateurBO:

    pass


class be_jebouquine_bo_ClientBO:

    pass


class be_jebouquine_bo_EtatCommandeBO:

    pass


class be_jebouquine_bo_PanierBO:

    def __init__(self, idPanier: int, quantity: int, date: date, listLivres: Collection_Livre_):
        self.idPanier = idPanier
        self.quantity = quantity
        self.date = date
        self.listLivres = listLivres
        
        pass
    @property
    def listLivres(self):
        return self.__listLivres
    @listLivres.setter
    def listLivres(self, listLivres: Collection_Livre_):
        self.__listLivres = listLivres

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def idPanier(self):
        return self.__idPanier
    @idPanier.setter
    def idPanier(self, idPanier: int):
        self.__idPanier = idPanier



class be_jebouquine_bo_CommentaireBO:

    pass


class be_jebouquine_bo_CommandeBO:

    pass


class be_jebouquine_bo_LivraisonTypeBO:

    pass


class be_jebouquine_bo_LangueBO:

    pass


class be_jebouquine_bo_CategorieBO:

    pass


class be_jebouquine_bo_LigneCommandeBO:

    pass


class be_jebouquine_bo_LivreBO:

    def __init__(self, idPanier: int):
        self.idPanier = idPanier
        
        pass
    @property
    def idPanier(self):
        return self.__idPanier
    @idPanier.setter
    def idPanier(self, idPanier: int):
        self.__idPanier = idPanier



class be_jebouquine_bo_AuteurBO:

    pass


class be_jebouquine_bo_EditeurBO:

    pass


class Collection_LigneCommande_:

    pass


class Collection_Livre_:

    pass


class Collection_Commentaire_:

    pass


class Collection_Commande_:

    pass


class Client:

    pass


class System_Component:

    pass


class be_jebouquine_entities_Commentaire:

    def __init__(self, idCommentaire: int, dateCommentaire: date, textCommentaire: str, idLivre: int, idClient: int, client23: "be_jebouquine_entities_Client" = None, livre29: "be_jebouquine_entities_Livre" = None):
        self.idCommentaire = idCommentaire
        self.dateCommentaire = dateCommentaire
        self.textCommentaire = textCommentaire
        self.idLivre = idLivre
        self.idClient = idClient
        self.client23 = client23
        self.livre29 = livre29
        
        pass
    @property
    def idLivre(self):
        return self.__idLivre
    @idLivre.setter
    def idLivre(self, idLivre: int):
        self.__idLivre = idLivre

    @property
    def idClient(self):
        return self.__idClient
    @idClient.setter
    def idClient(self, idClient: int):
        self.__idClient = idClient

    @property
    def textCommentaire(self):
        return self.__textCommentaire
    @textCommentaire.setter
    def textCommentaire(self, textCommentaire: str):
        self.__textCommentaire = textCommentaire

    @property
    def idCommentaire(self):
        return self.__idCommentaire
    @idCommentaire.setter
    def idCommentaire(self, idCommentaire: int):
        self.__idCommentaire = idCommentaire

    @property
    def dateCommentaire(self):
        return self.__dateCommentaire
    @dateCommentaire.setter
    def dateCommentaire(self, dateCommentaire: date):
        self.__dateCommentaire = dateCommentaire

    @property
    def client23(self):
        return self.__client23
    @client23.setter
    def client23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Commentaire__client23", None)
        self.__client23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commentaire22"):
                opp_val = getattr(old_value, "commentaire22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commentaire22"):
                opp_val = getattr(value, "commentaire22", None)
                if opp_val is None:
                    setattr(value, "commentaire22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def livre29(self):
        return self.__livre29
    @livre29.setter
    def livre29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Commentaire__livre29", None)
        self.__livre29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commentaire28"):
                opp_val = getattr(old_value, "commentaire28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commentaire28"):
                opp_val = getattr(value, "commentaire28", None)
                if opp_val is None:
                    setattr(value, "commentaire28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class be_jebouquine_entities_Langue:

    def __init__(self, idLangue: int, libelleLangue: str, livre26: set["be_jebouquine_entities_Livre"] = None):
        self.idLangue = idLangue
        self.libelleLangue = libelleLangue
        self.livre26 = livre26 if livre26 is not None else set()
        
        pass
    @property
    def idLangue(self):
        return self.__idLangue
    @idLangue.setter
    def idLangue(self, idLangue: int):
        self.__idLangue = idLangue

    @property
    def libelleLangue(self):
        return self.__libelleLangue
    @libelleLangue.setter
    def libelleLangue(self, libelleLangue: str):
        self.__libelleLangue = libelleLangue

    @property
    def livre26(self):
        return self.__livre26
    @livre26.setter
    def livre26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Langue__livre26", None)
        self.__livre26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "langue27"):
                    opp_val = getattr(item, "langue27", None)
                    
                    if opp_val == self:
                        setattr(item, "langue27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "langue27"):
                    opp_val = getattr(item, "langue27", None)
                    
                    setattr(item, "langue27", self)
                    



class be_jebouquine_entities_LigneCommande:

    def __init__(self, idLigneCommande: int, idLivre: int, idCommande: int, livre14: "be_jebouquine_entities_Livre" = None, commande33: "be_jebouquine_entities_Commande" = None):
        self.idLigneCommande = idLigneCommande
        self.idLivre = idLivre
        self.idCommande = idCommande
        self.livre14 = livre14
        self.commande33 = commande33
        
        pass
    @property
    def idLigneCommande(self):
        return self.__idLigneCommande
    @idLigneCommande.setter
    def idLigneCommande(self, idLigneCommande: int):
        self.__idLigneCommande = idLigneCommande

    @property
    def idLivre(self):
        return self.__idLivre
    @idLivre.setter
    def idLivre(self, idLivre: int):
        self.__idLivre = idLivre

    @property
    def idCommande(self):
        return self.__idCommande
    @idCommande.setter
    def idCommande(self, idCommande: int):
        self.__idCommande = idCommande

    @property
    def commande33(self):
        return self.__commande33
    @commande33.setter
    def commande33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_LigneCommande__commande33", None)
        self.__commande33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ligneCommande32"):
                opp_val = getattr(old_value, "ligneCommande32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ligneCommande32"):
                opp_val = getattr(value, "ligneCommande32", None)
                if opp_val is None:
                    setattr(value, "ligneCommande32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def livre14(self):
        return self.__livre14
    @livre14.setter
    def livre14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_LigneCommande__livre14", None)
        self.__livre14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ligneCommande15"):
                opp_val = getattr(old_value, "ligneCommande15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ligneCommande15"):
                opp_val = getattr(value, "ligneCommande15", None)
                if opp_val is None:
                    setattr(value, "ligneCommande15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class be_jebouquine_entities_LivraisonType:

    def __init__(self, idLivraison: int, typeLivraison: str, prixLivraison: float, commande35: set["be_jebouquine_entities_Commande"] = None):
        self.idLivraison = idLivraison
        self.typeLivraison = typeLivraison
        self.prixLivraison = prixLivraison
        self.commande35 = commande35 if commande35 is not None else set()
        
        pass
    @property
    def idLivraison(self):
        return self.__idLivraison
    @idLivraison.setter
    def idLivraison(self, idLivraison: int):
        self.__idLivraison = idLivraison

    @property
    def prixLivraison(self):
        return self.__prixLivraison
    @prixLivraison.setter
    def prixLivraison(self, prixLivraison: float):
        self.__prixLivraison = prixLivraison

    @property
    def typeLivraison(self):
        return self.__typeLivraison
    @typeLivraison.setter
    def typeLivraison(self, typeLivraison: str):
        self.__typeLivraison = typeLivraison

    @property
    def commande35(self):
        return self.__commande35
    @commande35.setter
    def commande35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_LivraisonType__commande35", None)
        self.__commande35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "livraisonInfo34"):
                    opp_val = getattr(item, "livraisonInfo34", None)
                    
                    if opp_val == self:
                        setattr(item, "livraisonInfo34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "livraisonInfo34"):
                    opp_val = getattr(item, "livraisonInfo34", None)
                    
                    setattr(item, "livraisonInfo34", self)
                    



class be_jebouquine_entities_EtatCommande:

    def __init__(self, idEtat: int, libelleEtat: str, commande25: set["be_jebouquine_entities_Commande"] = None):
        self.idEtat = idEtat
        self.libelleEtat = libelleEtat
        self.commande25 = commande25 if commande25 is not None else set()
        
        pass
    @property
    def libelleEtat(self):
        return self.__libelleEtat
    @libelleEtat.setter
    def libelleEtat(self, libelleEtat: str):
        self.__libelleEtat = libelleEtat

    @property
    def idEtat(self):
        return self.__idEtat
    @idEtat.setter
    def idEtat(self, idEtat: int):
        self.__idEtat = idEtat

    @property
    def commande25(self):
        return self.__commande25
    @commande25.setter
    def commande25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_EtatCommande__commande25", None)
        self.__commande25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etatCommande24"):
                    opp_val = getattr(item, "etatCommande24", None)
                    
                    if opp_val == self:
                        setattr(item, "etatCommande24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etatCommande24"):
                    opp_val = getattr(item, "etatCommande24", None)
                    
                    setattr(item, "etatCommande24", self)
                    



class be_jebouquine_entities_Commande:

    def __init__(self, idcommande: int, dateCommande: date, idEtat: int, idClient: int, idLivraisonInfo: int, client13: "be_jebouquine_entities_Client" = None, etatCommande24: "be_jebouquine_entities_EtatCommande" = None, ligneCommande32: set["be_jebouquine_entities_LigneCommande"] = None, livraisonInfo34: "be_jebouquine_entities_LivraisonType" = None):
        self.idcommande = idcommande
        self.dateCommande = dateCommande
        self.idEtat = idEtat
        self.idClient = idClient
        self.idLivraisonInfo = idLivraisonInfo
        self.client13 = client13
        self.etatCommande24 = etatCommande24
        self.ligneCommande32 = ligneCommande32 if ligneCommande32 is not None else set()
        self.livraisonInfo34 = livraisonInfo34
        
        pass
    @property
    def idLivraisonInfo(self):
        return self.__idLivraisonInfo
    @idLivraisonInfo.setter
    def idLivraisonInfo(self, idLivraisonInfo: int):
        self.__idLivraisonInfo = idLivraisonInfo

    @property
    def idEtat(self):
        return self.__idEtat
    @idEtat.setter
    def idEtat(self, idEtat: int):
        self.__idEtat = idEtat

    @property
    def dateCommande(self):
        return self.__dateCommande
    @dateCommande.setter
    def dateCommande(self, dateCommande: date):
        self.__dateCommande = dateCommande

    @property
    def idClient(self):
        return self.__idClient
    @idClient.setter
    def idClient(self, idClient: int):
        self.__idClient = idClient

    @property
    def idcommande(self):
        return self.__idcommande
    @idcommande.setter
    def idcommande(self, idcommande: int):
        self.__idcommande = idcommande

    @property
    def ligneCommande32(self):
        return self.__ligneCommande32
    @ligneCommande32.setter
    def ligneCommande32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Commande__ligneCommande32", None)
        self.__ligneCommande32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "commande33"):
                    opp_val = getattr(item, "commande33", None)
                    
                    if opp_val == self:
                        setattr(item, "commande33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "commande33"):
                    opp_val = getattr(item, "commande33", None)
                    
                    setattr(item, "commande33", self)
                    

    @property
    def etatCommande24(self):
        return self.__etatCommande24
    @etatCommande24.setter
    def etatCommande24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Commande__etatCommande24", None)
        self.__etatCommande24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commande25"):
                opp_val = getattr(old_value, "commande25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commande25"):
                opp_val = getattr(value, "commande25", None)
                if opp_val is None:
                    setattr(value, "commande25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def livraisonInfo34(self):
        return self.__livraisonInfo34
    @livraisonInfo34.setter
    def livraisonInfo34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Commande__livraisonInfo34", None)
        self.__livraisonInfo34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commande35"):
                opp_val = getattr(old_value, "commande35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commande35"):
                opp_val = getattr(value, "commande35", None)
                if opp_val is None:
                    setattr(value, "commande35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def client13(self):
        return self.__client13
    @client13.setter
    def client13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Commande__client13", None)
        self.__client13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commande12"):
                opp_val = getattr(old_value, "commande12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commande12"):
                opp_val = getattr(value, "commande12", None)
                if opp_val is None:
                    setattr(value, "commande12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class be_jebouquine_entities_Categorie:

    def __init__(self, idCategorie: int, ordreCategorie: str, livre21: "be_jebouquine_entities_Livre" = None):
        self.idCategorie = idCategorie
        self.ordreCategorie = ordreCategorie
        self.livre21 = livre21
        
        pass
    @property
    def idCategorie(self):
        return self.__idCategorie
    @idCategorie.setter
    def idCategorie(self, idCategorie: int):
        self.__idCategorie = idCategorie

    @property
    def ordreCategorie(self):
        return self.__ordreCategorie
    @ordreCategorie.setter
    def ordreCategorie(self, ordreCategorie: str):
        self.__ordreCategorie = ordreCategorie

    @property
    def livre21(self):
        return self.__livre21
    @livre21.setter
    def livre21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Categorie__livre21", None)
        self.__livre21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "categorie20"):
                opp_val = getattr(old_value, "categorie20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "categorie20"):
                opp_val = getattr(value, "categorie20", None)
                if opp_val is None:
                    setattr(value, "categorie20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class be_jebouquine_entities_Editeur:

    def __init__(self, idEditeur: int, nomEditeur: str, adresseEditeur: str, livre17: "be_jebouquine_entities_Livre" = None):
        self.idEditeur = idEditeur
        self.nomEditeur = nomEditeur
        self.adresseEditeur = adresseEditeur
        self.livre17 = livre17
        
        pass
    @property
    def adresseEditeur(self):
        return self.__adresseEditeur
    @adresseEditeur.setter
    def adresseEditeur(self, adresseEditeur: str):
        self.__adresseEditeur = adresseEditeur

    @property
    def idEditeur(self):
        return self.__idEditeur
    @idEditeur.setter
    def idEditeur(self, idEditeur: int):
        self.__idEditeur = idEditeur

    @property
    def nomEditeur(self):
        return self.__nomEditeur
    @nomEditeur.setter
    def nomEditeur(self, nomEditeur: str):
        self.__nomEditeur = nomEditeur

    @property
    def livre17(self):
        return self.__livre17
    @livre17.setter
    def livre17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Editeur__livre17", None)
        self.__livre17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editeur16"):
                opp_val = getattr(old_value, "editeur16", None)
                if opp_val == self:
                    setattr(old_value, "editeur16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editeur16"):
                opp_val = getattr(value, "editeur16", None)
                setattr(value, "editeur16", self)



class be_jebouquine_entities_Auteur:

    def __init__(self, idAuteur: int, nomAuteur: str, livre19: "be_jebouquine_entities_Livre" = None):
        self.idAuteur = idAuteur
        self.nomAuteur = nomAuteur
        self.livre19 = livre19
        
        pass
    @property
    def idAuteur(self):
        return self.__idAuteur
    @idAuteur.setter
    def idAuteur(self, idAuteur: int):
        self.__idAuteur = idAuteur

    @property
    def nomAuteur(self):
        return self.__nomAuteur
    @nomAuteur.setter
    def nomAuteur(self, nomAuteur: str):
        self.__nomAuteur = nomAuteur

    @property
    def livre19(self):
        return self.__livre19
    @livre19.setter
    def livre19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Auteur__livre19", None)
        self.__livre19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auteur18"):
                opp_val = getattr(old_value, "auteur18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auteur18"):
                opp_val = getattr(value, "auteur18", None)
                if opp_val is None:
                    setattr(value, "auteur18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class be_jebouquine_entities_Livre:

    def __init__(self, idLivre: int, titre: str, dateApparition: date, prix: float, quantiteEnStock: int, isbn: str, photoLivre: str, idLangue: int, idAuteur: int, idEditeur: int, idCategorie: int, ligneCommande15: set["be_jebouquine_entities_LigneCommande"] = None, editeur16: "be_jebouquine_entities_Editeur" = None, auteur18: set["be_jebouquine_entities_Auteur"] = None, categorie20: set["be_jebouquine_entities_Categorie"] = None, langue27: "be_jebouquine_entities_Langue" = None, commentaire28: set["be_jebouquine_entities_Commentaire"] = None):
        self.idLivre = idLivre
        self.titre = titre
        self.dateApparition = dateApparition
        self.prix = prix
        self.quantiteEnStock = quantiteEnStock
        self.isbn = isbn
        self.photoLivre = photoLivre
        self.idLangue = idLangue
        self.idAuteur = idAuteur
        self.idEditeur = idEditeur
        self.idCategorie = idCategorie
        self.ligneCommande15 = ligneCommande15 if ligneCommande15 is not None else set()
        self.editeur16 = editeur16
        self.auteur18 = auteur18 if auteur18 is not None else set()
        self.categorie20 = categorie20 if categorie20 is not None else set()
        self.langue27 = langue27
        self.commentaire28 = commentaire28 if commentaire28 is not None else set()
        
        pass
    @property
    def idLangue(self):
        return self.__idLangue
    @idLangue.setter
    def idLangue(self, idLangue: int):
        self.__idLangue = idLangue

    @property
    def idEditeur(self):
        return self.__idEditeur
    @idEditeur.setter
    def idEditeur(self, idEditeur: int):
        self.__idEditeur = idEditeur

    @property
    def photoLivre(self):
        return self.__photoLivre
    @photoLivre.setter
    def photoLivre(self, photoLivre: str):
        self.__photoLivre = photoLivre

    @property
    def dateApparition(self):
        return self.__dateApparition
    @dateApparition.setter
    def dateApparition(self, dateApparition: date):
        self.__dateApparition = dateApparition

    @property
    def idLivre(self):
        return self.__idLivre
    @idLivre.setter
    def idLivre(self, idLivre: int):
        self.__idLivre = idLivre

    @property
    def quantiteEnStock(self):
        return self.__quantiteEnStock
    @quantiteEnStock.setter
    def quantiteEnStock(self, quantiteEnStock: int):
        self.__quantiteEnStock = quantiteEnStock

    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self, prix: float):
        self.__prix = prix

    @property
    def isbn(self):
        return self.__isbn
    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def idCategorie(self):
        return self.__idCategorie
    @idCategorie.setter
    def idCategorie(self, idCategorie: int):
        self.__idCategorie = idCategorie

    @property
    def idAuteur(self):
        return self.__idAuteur
    @idAuteur.setter
    def idAuteur(self, idAuteur: int):
        self.__idAuteur = idAuteur

    @property
    def titre(self):
        return self.__titre
    @titre.setter
    def titre(self, titre: str):
        self.__titre = titre

    @property
    def categorie20(self):
        return self.__categorie20
    @categorie20.setter
    def categorie20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Livre__categorie20", None)
        self.__categorie20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "livre21"):
                    opp_val = getattr(item, "livre21", None)
                    
                    if opp_val == self:
                        setattr(item, "livre21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "livre21"):
                    opp_val = getattr(item, "livre21", None)
                    
                    setattr(item, "livre21", self)
                    

    @property
    def langue27(self):
        return self.__langue27
    @langue27.setter
    def langue27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Livre__langue27", None)
        self.__langue27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "livre26"):
                opp_val = getattr(old_value, "livre26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "livre26"):
                opp_val = getattr(value, "livre26", None)
                if opp_val is None:
                    setattr(value, "livre26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ligneCommande15(self):
        return self.__ligneCommande15
    @ligneCommande15.setter
    def ligneCommande15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Livre__ligneCommande15", None)
        self.__ligneCommande15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "livre14"):
                    opp_val = getattr(item, "livre14", None)
                    
                    if opp_val == self:
                        setattr(item, "livre14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "livre14"):
                    opp_val = getattr(item, "livre14", None)
                    
                    setattr(item, "livre14", self)
                    

    @property
    def commentaire28(self):
        return self.__commentaire28
    @commentaire28.setter
    def commentaire28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Livre__commentaire28", None)
        self.__commentaire28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "livre29"):
                    opp_val = getattr(item, "livre29", None)
                    
                    if opp_val == self:
                        setattr(item, "livre29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "livre29"):
                    opp_val = getattr(item, "livre29", None)
                    
                    setattr(item, "livre29", self)
                    

    @property
    def auteur18(self):
        return self.__auteur18
    @auteur18.setter
    def auteur18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Livre__auteur18", None)
        self.__auteur18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "livre19"):
                    opp_val = getattr(item, "livre19", None)
                    
                    if opp_val == self:
                        setattr(item, "livre19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "livre19"):
                    opp_val = getattr(item, "livre19", None)
                    
                    setattr(item, "livre19", self)
                    

    @property
    def editeur16(self):
        return self.__editeur16
    @editeur16.setter
    def editeur16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Livre__editeur16", None)
        self.__editeur16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "livre17"):
                opp_val = getattr(old_value, "livre17", None)
                if opp_val == self:
                    setattr(old_value, "livre17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "livre17"):
                opp_val = getattr(value, "livre17", None)
                setattr(value, "livre17", self)



class be_jebouquine_entities_Administrateur:

    def __init__(self, idAdministrateur: int, nomAdministrateur: str, emailAdministrateur: str, motDePasseAdministrateur: str, prenomAdministrateur: str):
        self.idAdministrateur = idAdministrateur
        self.nomAdministrateur = nomAdministrateur
        self.emailAdministrateur = emailAdministrateur
        self.motDePasseAdministrateur = motDePasseAdministrateur
        self.prenomAdministrateur = prenomAdministrateur
        
        pass
    @property
    def idAdministrateur(self):
        return self.__idAdministrateur
    @idAdministrateur.setter
    def idAdministrateur(self, idAdministrateur: int):
        self.__idAdministrateur = idAdministrateur

    @property
    def prenomAdministrateur(self):
        return self.__prenomAdministrateur
    @prenomAdministrateur.setter
    def prenomAdministrateur(self, prenomAdministrateur: str):
        self.__prenomAdministrateur = prenomAdministrateur

    @property
    def emailAdministrateur(self):
        return self.__emailAdministrateur
    @emailAdministrateur.setter
    def emailAdministrateur(self, emailAdministrateur: str):
        self.__emailAdministrateur = emailAdministrateur

    @property
    def motDePasseAdministrateur(self):
        return self.__motDePasseAdministrateur
    @motDePasseAdministrateur.setter
    def motDePasseAdministrateur(self, motDePasseAdministrateur: str):
        self.__motDePasseAdministrateur = motDePasseAdministrateur

    @property
    def nomAdministrateur(self):
        return self.__nomAdministrateur
    @nomAdministrateur.setter
    def nomAdministrateur(self, nomAdministrateur: str):
        self.__nomAdministrateur = nomAdministrateur



class be_jebouquine_entities_Client:

    def __init__(self, idClient: int, nomClient: str, adresseClient: str, emailClient: str, telephoneClient: str, motDePasseClient: str, etatLogin: str, commande12: set["be_jebouquine_entities_Commande"] = None, commentaire22: set["be_jebouquine_entities_Commentaire"] = None):
        self.idClient = idClient
        self.nomClient = nomClient
        self.adresseClient = adresseClient
        self.emailClient = emailClient
        self.telephoneClient = telephoneClient
        self.motDePasseClient = motDePasseClient
        self.etatLogin = etatLogin
        self.commande12 = commande12 if commande12 is not None else set()
        self.commentaire22 = commentaire22 if commentaire22 is not None else set()
        
        pass
    @property
    def adresseClient(self):
        return self.__adresseClient
    @adresseClient.setter
    def adresseClient(self, adresseClient: str):
        self.__adresseClient = adresseClient

    @property
    def idClient(self):
        return self.__idClient
    @idClient.setter
    def idClient(self, idClient: int):
        self.__idClient = idClient

    @property
    def motDePasseClient(self):
        return self.__motDePasseClient
    @motDePasseClient.setter
    def motDePasseClient(self, motDePasseClient: str):
        self.__motDePasseClient = motDePasseClient

    @property
    def nomClient(self):
        return self.__nomClient
    @nomClient.setter
    def nomClient(self, nomClient: str):
        self.__nomClient = nomClient

    @property
    def telephoneClient(self):
        return self.__telephoneClient
    @telephoneClient.setter
    def telephoneClient(self, telephoneClient: str):
        self.__telephoneClient = telephoneClient

    @property
    def etatLogin(self):
        return self.__etatLogin
    @etatLogin.setter
    def etatLogin(self, etatLogin: str):
        self.__etatLogin = etatLogin

    @property
    def emailClient(self):
        return self.__emailClient
    @emailClient.setter
    def emailClient(self, emailClient: str):
        self.__emailClient = emailClient

    @property
    def commentaire22(self):
        return self.__commentaire22
    @commentaire22.setter
    def commentaire22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Client__commentaire22", None)
        self.__commentaire22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "client23"):
                    opp_val = getattr(item, "client23", None)
                    
                    if opp_val == self:
                        setattr(item, "client23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "client23"):
                    opp_val = getattr(item, "client23", None)
                    
                    setattr(item, "client23", self)
                    

    @property
    def commande12(self):
        return self.__commande12
    @commande12.setter
    def commande12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_be_jebouquine_entities_Client__commande12", None)
        self.__commande12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "client13"):
                    opp_val = getattr(item, "client13", None)
                    
                    if opp_val == self:
                        setattr(item, "client13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "client13"):
                    opp_val = getattr(item, "client13", None)
                    
                    setattr(item, "client13", self)
                    

