####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
commande_Suivre_commande_UseCase = Class(name="commande_Suivre_commande_UseCase")
commande_Annuler_commande_UseCase = Class(name="commande_Annuler_commande_UseCase")
navigation_Parcourir_les_livres_UseCase = Class(name="navigation_Parcourir_les_livres_UseCase")
navigation_Rechercher_un_livre_UseCase = Class(name="navigation_Rechercher_un_livre_UseCase")
panier_Ajouter_au_panier_UseCase = Class(name="panier_Ajouter_au_panier_UseCase")
panier_Supprimer_du_panier_UseCase = Class(name="panier_Supprimer_du_panier_UseCase")
panier_Gerer_panier_UseCase = Class(name="panier_Gerer_panier_UseCase")
panier_Modifier_quantite_livre_UseCase = Class(name="panier_Modifier_quantite_livre_UseCase")
panier_Passer_une_commande_UseCase = Class(name="panier_Passer_une_commande_UseCase")
information_Consulter_l_aide_UseCase = Class(name="information_Consulter_l_aide_UseCase")
navigation_Recherche_par_critere_UseCase = Class(name="navigation_Recherche_par_critere_UseCase")
navigation_Afficher_la_liste_des_livres_UseCase = Class(name="navigation_Afficher_la_liste_des_livres_UseCase")
be_jebouquine_entities_Client = Class(name="be_jebouquine_entities_Client")
be_jebouquine_entities_Administrateur = Class(name="be_jebouquine_entities_Administrateur")
be_jebouquine_entities_Livre = Class(name="be_jebouquine_entities_Livre")
be_jebouquine_entities_Auteur = Class(name="be_jebouquine_entities_Auteur")
be_jebouquine_entities_Editeur = Class(name="be_jebouquine_entities_Editeur")
be_jebouquine_entities_Categorie = Class(name="be_jebouquine_entities_Categorie")
be_jebouquine_entities_Commande = Class(name="be_jebouquine_entities_Commande")
be_jebouquine_entities_EtatCommande = Class(name="be_jebouquine_entities_EtatCommande")
be_jebouquine_entities_LivraisonType = Class(name="be_jebouquine_entities_LivraisonType")
be_jebouquine_entities_LigneCommande = Class(name="be_jebouquine_entities_LigneCommande")
be_jebouquine_entities_Langue = Class(name="be_jebouquine_entities_Langue")
be_jebouquine_entities_Commentaire = Class(name="be_jebouquine_entities_Commentaire")
backoffice_Gerer_les_produits_UseCase = Class(name="backoffice_Gerer_les_produits_UseCase")
backoffice_S_authentifier_UseCase = Class(name="backoffice_S_authentifier_UseCase")
backoffice_Gerer_les_categories_UseCase = Class(name="backoffice_Gerer_les_categories_UseCase")
backoffice_Valider_les_commentaires_UseCase = Class(name="backoffice_Valider_les_commentaires_UseCase")
backoffice_Gerer_les_editeurs_UseCase = Class(name="backoffice_Gerer_les_editeurs_UseCase")
backoffice_Gerer_les_auteurs_UseCase = Class(name="backoffice_Gerer_les_auteurs_UseCase")
System_Component = Class(name="System_Component")
Client = Class(name="Client")
Collection_Commande_ = Class(name="Collection_Commande_")
Collection_Commentaire_ = Class(name="Collection_Commentaire_")
Collection_Livre_ = Class(name="Collection_Livre_")
Collection_LigneCommande_ = Class(name="Collection_LigneCommande_")
be_jebouquine_bo_EditeurBO = Class(name="be_jebouquine_bo_EditeurBO")
be_jebouquine_bo_AuteurBO = Class(name="be_jebouquine_bo_AuteurBO")
be_jebouquine_bo_LivreBO = Class(name="be_jebouquine_bo_LivreBO")
be_jebouquine_bo_LigneCommandeBO = Class(name="be_jebouquine_bo_LigneCommandeBO")
be_jebouquine_bo_CategorieBO = Class(name="be_jebouquine_bo_CategorieBO")
be_jebouquine_bo_LangueBO = Class(name="be_jebouquine_bo_LangueBO")
be_jebouquine_bo_LivraisonTypeBO = Class(name="be_jebouquine_bo_LivraisonTypeBO")
be_jebouquine_bo_CommandeBO = Class(name="be_jebouquine_bo_CommandeBO")
be_jebouquine_bo_CommentaireBO = Class(name="be_jebouquine_bo_CommentaireBO")
be_jebouquine_bo_PanierBO = Class(name="be_jebouquine_bo_PanierBO")
be_jebouquine_bo_EtatCommandeBO = Class(name="be_jebouquine_bo_EtatCommandeBO")
be_jebouquine_bo_ClientBO = Class(name="be_jebouquine_bo_ClientBO")
be_jebouquine_bo_AdministrateurBO = Class(name="be_jebouquine_bo_AdministrateurBO")
be_jebouquine_bo_ICommandeBORemote_Interface = Class(name="be_jebouquine_bo_ICommandeBORemote_Interface")
be_jebouquine_bo_ILangueBORemote_Interface = Class(name="be_jebouquine_bo_ILangueBORemote_Interface")
be_jebouquine_bo_IClientBORemote_Interface = Class(name="be_jebouquine_bo_IClientBORemote_Interface")
be_jebouquine_bo_ICommentaireBORemote_Interface = Class(name="be_jebouquine_bo_ICommentaireBORemote_Interface")
be_jebouquine_bo_IEditeurBORemote_Interface = Class(name="be_jebouquine_bo_IEditeurBORemote_Interface")
be_jebouquine_bo_ILivreBORemote_Interface = Class(name="be_jebouquine_bo_ILivreBORemote_Interface")
be_jebouquine_bo_IAuteurBORemote_Interface = Class(name="be_jebouquine_bo_IAuteurBORemote_Interface")
be_jebouquine_bo_IPanierBORemote_Interface = Class(name="be_jebouquine_bo_IPanierBORemote_Interface")
be_jebouquine_bo_LivraisonTypeBORemote_Interface = Class(name="be_jebouquine_bo_LivraisonTypeBORemote_Interface")
be_jebouquine_bo_IAdministrateurBORemote_Interface = Class(name="be_jebouquine_bo_IAdministrateurBORemote_Interface")
be_jebouquine_bo_LigneCommandeBORemote_Interface = Class(name="be_jebouquine_bo_LigneCommandeBORemote_Interface")
be_jebouquine_bo_IEtatCommandeRemote_Interface = Class(name="be_jebouquine_bo_IEtatCommandeRemote_Interface")
be_jebouquine_bo_ICategorieBORemote_Interface = Class(name="be_jebouquine_bo_ICategorieBORemote_Interface")
Collection_Client_ = Class(name="Collection_Client_")
Object = Class(name="Object")
Collection_Object_ = Class(name="Collection_Object_")
be_jebouquine_dao_AbstractFactory = Class(name="be_jebouquine_dao_AbstractFactory", is_abstract=True)
be_jebouquine_dao_AdministrateurDAO = Class(name="be_jebouquine_dao_AdministrateurDAO")
be_jebouquine_dao_AuteurDAO = Class(name="be_jebouquine_dao_AuteurDAO")
be_jebouquine_dao_LangueDAO = Class(name="be_jebouquine_dao_LangueDAO")
be_jebouquine_dao_EditeurDAO = Class(name="be_jebouquine_dao_EditeurDAO")
be_jebouquine_dao_LivreDAO = Class(name="be_jebouquine_dao_LivreDAO")
be_jebouquine_dao_LivraisonInfoDAO = Class(name="be_jebouquine_dao_LivraisonInfoDAO")
be_jebouquine_dao_CategorieDAO = Class(name="be_jebouquine_dao_CategorieDAO")
be_jebouquine_dao_CommentaireDAO = Class(name="be_jebouquine_dao_CommentaireDAO")
be_jebouquine_dao_LigneCommandeDAO = Class(name="be_jebouquine_dao_LigneCommandeDAO")
be_jebouquine_dao_ClientDAO = Class(name="be_jebouquine_dao_ClientDAO")
be_jebouquine_dao_CommandeDAO = Class(name="be_jebouquine_dao_CommandeDAO")
be_jebouquine_dao_EtatCommandeDAO = Class(name="be_jebouquine_dao_EtatCommandeDAO")
Client_Actor = Class(name="Client_Actor")
Visiteur_Actor = Class(name="Visiteur_Actor")
Administrateur_Actor = Class(name="Administrateur_Actor")
Systeme_Paiement_Actor = Class(name="Systeme_Paiement_Actor")
compte_Gerer_le_compte_UseCase = Class(name="compte_Gerer_le_compte_UseCase")
compte_Ajouter_commentaire_UseCase = Class(name="compte_Ajouter_commentaire_UseCase")
compte_S_authentifier_UseCase = Class(name="compte_S_authentifier_UseCase")
compte_Gerer_Commande_UseCase = Class(name="compte_Gerer_Commande_UseCase")
commande_Creer_commande_UseCase = Class(name="commande_Creer_commande_UseCase")
commande_Payer_commande_UseCase = Class(name="commande_Payer_commande_UseCase")

# commande_Suivre_commande_UseCase class attributes and methods

# commande_Annuler_commande_UseCase class attributes and methods

# navigation_Parcourir_les_livres_UseCase class attributes and methods

# navigation_Rechercher_un_livre_UseCase class attributes and methods

# panier_Ajouter_au_panier_UseCase class attributes and methods

# panier_Supprimer_du_panier_UseCase class attributes and methods

# panier_Gerer_panier_UseCase class attributes and methods

# panier_Modifier_quantite_livre_UseCase class attributes and methods

# panier_Passer_une_commande_UseCase class attributes and methods

# information_Consulter_l_aide_UseCase class attributes and methods

# navigation_Recherche_par_critere_UseCase class attributes and methods

# navigation_Afficher_la_liste_des_livres_UseCase class attributes and methods

# be_jebouquine_entities_Client class attributes and methods
be_jebouquine_entities_Client_idClient: Property = Property(name="idClient", type=IntegerType)
be_jebouquine_entities_Client_nomClient: Property = Property(name="nomClient", type=StringType)
be_jebouquine_entities_Client_adresseClient: Property = Property(name="adresseClient", type=StringType)
be_jebouquine_entities_Client_emailClient: Property = Property(name="emailClient", type=StringType)
be_jebouquine_entities_Client_telephoneClient: Property = Property(name="telephoneClient", type=StringType)
be_jebouquine_entities_Client_motDePasseClient: Property = Property(name="motDePasseClient", type=StringType)
be_jebouquine_entities_Client_etatLogin: Property = Property(name="etatLogin", type=StringType)
be_jebouquine_entities_Client.attributes={be_jebouquine_entities_Client_emailClient, be_jebouquine_entities_Client_adresseClient, be_jebouquine_entities_Client_motDePasseClient, be_jebouquine_entities_Client_idClient, be_jebouquine_entities_Client_nomClient, be_jebouquine_entities_Client_telephoneClient, be_jebouquine_entities_Client_etatLogin}

# be_jebouquine_entities_Administrateur class attributes and methods
be_jebouquine_entities_Administrateur_idAdministrateur: Property = Property(name="idAdministrateur", type=IntegerType)
be_jebouquine_entities_Administrateur_nomAdministrateur: Property = Property(name="nomAdministrateur", type=StringType)
be_jebouquine_entities_Administrateur_emailAdministrateur: Property = Property(name="emailAdministrateur", type=StringType)
be_jebouquine_entities_Administrateur_motDePasseAdministrateur: Property = Property(name="motDePasseAdministrateur", type=StringType)
be_jebouquine_entities_Administrateur_prenomAdministrateur: Property = Property(name="prenomAdministrateur", type=StringType)
be_jebouquine_entities_Administrateur.attributes={be_jebouquine_entities_Administrateur_idAdministrateur, be_jebouquine_entities_Administrateur_nomAdministrateur, be_jebouquine_entities_Administrateur_emailAdministrateur, be_jebouquine_entities_Administrateur_prenomAdministrateur, be_jebouquine_entities_Administrateur_motDePasseAdministrateur}

# be_jebouquine_entities_Livre class attributes and methods
be_jebouquine_entities_Livre_idLivre: Property = Property(name="idLivre", type=IntegerType)
be_jebouquine_entities_Livre_titre: Property = Property(name="titre", type=StringType)
be_jebouquine_entities_Livre_dateApparition: Property = Property(name="dateApparition", type=DateType)
be_jebouquine_entities_Livre_prix: Property = Property(name="prix", type=FloatType)
be_jebouquine_entities_Livre_quantiteEnStock: Property = Property(name="quantiteEnStock", type=IntegerType)
be_jebouquine_entities_Livre_isbn: Property = Property(name="isbn", type=StringType)
be_jebouquine_entities_Livre_photoLivre: Property = Property(name="photoLivre", type=StringType)
be_jebouquine_entities_Livre_idLangue: Property = Property(name="idLangue", type=IntegerType)
be_jebouquine_entities_Livre_idAuteur: Property = Property(name="idAuteur", type=IntegerType)
be_jebouquine_entities_Livre_idEditeur: Property = Property(name="idEditeur", type=IntegerType)
be_jebouquine_entities_Livre_idCategorie: Property = Property(name="idCategorie", type=IntegerType)
be_jebouquine_entities_Livre.attributes={be_jebouquine_entities_Livre_prix, be_jebouquine_entities_Livre_photoLivre, be_jebouquine_entities_Livre_titre, be_jebouquine_entities_Livre_isbn, be_jebouquine_entities_Livre_idLangue, be_jebouquine_entities_Livre_quantiteEnStock, be_jebouquine_entities_Livre_idCategorie, be_jebouquine_entities_Livre_idAuteur, be_jebouquine_entities_Livre_idEditeur, be_jebouquine_entities_Livre_dateApparition, be_jebouquine_entities_Livre_idLivre}

# be_jebouquine_entities_Auteur class attributes and methods
be_jebouquine_entities_Auteur_idAuteur: Property = Property(name="idAuteur", type=IntegerType)
be_jebouquine_entities_Auteur_nomAuteur: Property = Property(name="nomAuteur", type=StringType)
be_jebouquine_entities_Auteur.attributes={be_jebouquine_entities_Auteur_idAuteur, be_jebouquine_entities_Auteur_nomAuteur}

# be_jebouquine_entities_Editeur class attributes and methods
be_jebouquine_entities_Editeur_idEditeur: Property = Property(name="idEditeur", type=IntegerType)
be_jebouquine_entities_Editeur_nomEditeur: Property = Property(name="nomEditeur", type=StringType)
be_jebouquine_entities_Editeur_adresseEditeur: Property = Property(name="adresseEditeur", type=StringType)
be_jebouquine_entities_Editeur.attributes={be_jebouquine_entities_Editeur_idEditeur, be_jebouquine_entities_Editeur_adresseEditeur, be_jebouquine_entities_Editeur_nomEditeur}

# be_jebouquine_entities_Categorie class attributes and methods
be_jebouquine_entities_Categorie_idCategorie: Property = Property(name="idCategorie", type=IntegerType)
be_jebouquine_entities_Categorie_ordreCategorie: Property = Property(name="ordreCategorie", type=StringType)
be_jebouquine_entities_Categorie.attributes={be_jebouquine_entities_Categorie_idCategorie, be_jebouquine_entities_Categorie_ordreCategorie}

# be_jebouquine_entities_Commande class attributes and methods
be_jebouquine_entities_Commande_idcommande: Property = Property(name="idcommande", type=IntegerType)
be_jebouquine_entities_Commande_dateCommande: Property = Property(name="dateCommande", type=DateType)
be_jebouquine_entities_Commande_idEtat: Property = Property(name="idEtat", type=IntegerType)
be_jebouquine_entities_Commande_idClient: Property = Property(name="idClient", type=IntegerType)
be_jebouquine_entities_Commande_idLivraisonInfo: Property = Property(name="idLivraisonInfo", type=IntegerType)
be_jebouquine_entities_Commande.attributes={be_jebouquine_entities_Commande_idcommande, be_jebouquine_entities_Commande_idEtat, be_jebouquine_entities_Commande_dateCommande, be_jebouquine_entities_Commande_idClient, be_jebouquine_entities_Commande_idLivraisonInfo}

# be_jebouquine_entities_EtatCommande class attributes and methods
be_jebouquine_entities_EtatCommande_idEtat: Property = Property(name="idEtat", type=IntegerType)
be_jebouquine_entities_EtatCommande_libelleEtat: Property = Property(name="libelleEtat", type=StringType)
be_jebouquine_entities_EtatCommande.attributes={be_jebouquine_entities_EtatCommande_libelleEtat, be_jebouquine_entities_EtatCommande_idEtat}

# be_jebouquine_entities_LivraisonType class attributes and methods
be_jebouquine_entities_LivraisonType_idLivraison: Property = Property(name="idLivraison", type=IntegerType)
be_jebouquine_entities_LivraisonType_typeLivraison: Property = Property(name="typeLivraison", type=StringType)
be_jebouquine_entities_LivraisonType_prixLivraison: Property = Property(name="prixLivraison", type=FloatType)
be_jebouquine_entities_LivraisonType.attributes={be_jebouquine_entities_LivraisonType_prixLivraison, be_jebouquine_entities_LivraisonType_idLivraison, be_jebouquine_entities_LivraisonType_typeLivraison}

# be_jebouquine_entities_LigneCommande class attributes and methods
be_jebouquine_entities_LigneCommande_idLigneCommande: Property = Property(name="idLigneCommande", type=IntegerType)
be_jebouquine_entities_LigneCommande_idLivre: Property = Property(name="idLivre", type=IntegerType)
be_jebouquine_entities_LigneCommande_idCommande: Property = Property(name="idCommande", type=IntegerType)
be_jebouquine_entities_LigneCommande.attributes={be_jebouquine_entities_LigneCommande_idLivre, be_jebouquine_entities_LigneCommande_idCommande, be_jebouquine_entities_LigneCommande_idLigneCommande}

# be_jebouquine_entities_Langue class attributes and methods
be_jebouquine_entities_Langue_idLangue: Property = Property(name="idLangue", type=IntegerType)
be_jebouquine_entities_Langue_libelleLangue: Property = Property(name="libelleLangue", type=StringType)
be_jebouquine_entities_Langue.attributes={be_jebouquine_entities_Langue_idLangue, be_jebouquine_entities_Langue_libelleLangue}

# be_jebouquine_entities_Commentaire class attributes and methods
be_jebouquine_entities_Commentaire_idCommentaire: Property = Property(name="idCommentaire", type=IntegerType)
be_jebouquine_entities_Commentaire_dateCommentaire: Property = Property(name="dateCommentaire", type=DateType)
be_jebouquine_entities_Commentaire_textCommentaire: Property = Property(name="textCommentaire", type=StringType)
be_jebouquine_entities_Commentaire_idLivre: Property = Property(name="idLivre", type=IntegerType)
be_jebouquine_entities_Commentaire_idClient: Property = Property(name="idClient", type=IntegerType)
be_jebouquine_entities_Commentaire.attributes={be_jebouquine_entities_Commentaire_textCommentaire, be_jebouquine_entities_Commentaire_dateCommentaire, be_jebouquine_entities_Commentaire_idCommentaire, be_jebouquine_entities_Commentaire_idClient, be_jebouquine_entities_Commentaire_idLivre}

# backoffice_Gerer_les_produits_UseCase class attributes and methods

# backoffice_S_authentifier_UseCase class attributes and methods

# backoffice_Gerer_les_categories_UseCase class attributes and methods

# backoffice_Valider_les_commentaires_UseCase class attributes and methods

# backoffice_Gerer_les_editeurs_UseCase class attributes and methods

# backoffice_Gerer_les_auteurs_UseCase class attributes and methods

# System_Component class attributes and methods

# Client class attributes and methods

# Collection_Commande_ class attributes and methods

# Collection_Commentaire_ class attributes and methods

# Collection_Livre_ class attributes and methods

# Collection_LigneCommande_ class attributes and methods

# be_jebouquine_bo_EditeurBO class attributes and methods

# be_jebouquine_bo_AuteurBO class attributes and methods

# be_jebouquine_bo_LivreBO class attributes and methods
be_jebouquine_bo_LivreBO_idPanier: Property = Property(name="idPanier", type=IntegerType)
be_jebouquine_bo_LivreBO.attributes={be_jebouquine_bo_LivreBO_idPanier}

# be_jebouquine_bo_LigneCommandeBO class attributes and methods

# be_jebouquine_bo_CategorieBO class attributes and methods

# be_jebouquine_bo_LangueBO class attributes and methods

# be_jebouquine_bo_LivraisonTypeBO class attributes and methods

# be_jebouquine_bo_CommandeBO class attributes and methods

# be_jebouquine_bo_CommentaireBO class attributes and methods

# be_jebouquine_bo_PanierBO class attributes and methods
be_jebouquine_bo_PanierBO_idPanier: Property = Property(name="idPanier", type=IntegerType)
be_jebouquine_bo_PanierBO_quantity: Property = Property(name="quantity", type=IntegerType)
be_jebouquine_bo_PanierBO_date: Property = Property(name="date", type=DateType)
be_jebouquine_bo_PanierBO_listLivres: Property = Property(name="listLivres", type=Collection_Livre_)
be_jebouquine_bo_PanierBO.attributes={be_jebouquine_bo_PanierBO_listLivres, be_jebouquine_bo_PanierBO_idPanier, be_jebouquine_bo_PanierBO_date, be_jebouquine_bo_PanierBO_quantity}

# be_jebouquine_bo_EtatCommandeBO class attributes and methods

# be_jebouquine_bo_ClientBO class attributes and methods

# be_jebouquine_bo_AdministrateurBO class attributes and methods

# be_jebouquine_bo_ICommandeBORemote_Interface class attributes and methods

# be_jebouquine_bo_ILangueBORemote_Interface class attributes and methods

# be_jebouquine_bo_IClientBORemote_Interface class attributes and methods

# be_jebouquine_bo_ICommentaireBORemote_Interface class attributes and methods

# be_jebouquine_bo_IEditeurBORemote_Interface class attributes and methods

# be_jebouquine_bo_ILivreBORemote_Interface class attributes and methods

# be_jebouquine_bo_IAuteurBORemote_Interface class attributes and methods

# be_jebouquine_bo_IPanierBORemote_Interface class attributes and methods

# be_jebouquine_bo_LivraisonTypeBORemote_Interface class attributes and methods

# be_jebouquine_bo_IAdministrateurBORemote_Interface class attributes and methods

# be_jebouquine_bo_LigneCommandeBORemote_Interface class attributes and methods

# be_jebouquine_bo_IEtatCommandeRemote_Interface class attributes and methods

# be_jebouquine_bo_ICategorieBORemote_Interface class attributes and methods

# Collection_Client_ class attributes and methods

# Object class attributes and methods

# Collection_Object_ class attributes and methods

# be_jebouquine_dao_AbstractFactory class attributes and methods

# be_jebouquine_dao_AdministrateurDAO class attributes and methods

# be_jebouquine_dao_AuteurDAO class attributes and methods

# be_jebouquine_dao_LangueDAO class attributes and methods

# be_jebouquine_dao_EditeurDAO class attributes and methods

# be_jebouquine_dao_LivreDAO class attributes and methods

# be_jebouquine_dao_LivraisonInfoDAO class attributes and methods

# be_jebouquine_dao_CategorieDAO class attributes and methods

# be_jebouquine_dao_CommentaireDAO class attributes and methods

# be_jebouquine_dao_LigneCommandeDAO class attributes and methods

# be_jebouquine_dao_ClientDAO class attributes and methods

# be_jebouquine_dao_CommandeDAO class attributes and methods

# be_jebouquine_dao_EtatCommandeDAO class attributes and methods

# Client_Actor class attributes and methods

# Visiteur_Actor class attributes and methods

# Administrateur_Actor class attributes and methods

# Systeme_Paiement_Actor class attributes and methods

# compte_Gerer_le_compte_UseCase class attributes and methods

# compte_Ajouter_commentaire_UseCase class attributes and methods

# compte_S_authentifier_UseCase class attributes and methods

# compte_Gerer_Commande_UseCase class attributes and methods

# commande_Creer_commande_UseCase class attributes and methods

# commande_Payer_commande_UseCase class attributes and methods

# Relationships
Client_S_authentifier: BinaryAssociation = BinaryAssociation(
    name="Client_S_authentifier",
    ends={
        Property(name="client5", type=Client_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="s_authentifier4", type=compte_S_authentifier_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Parcourir_les_livres_Visiteur: BinaryAssociation = BinaryAssociation(
    name="Parcourir_les_livres_Visiteur",
    ends={
        Property(name="visiteur6", type=Visiteur_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="parcourir_les_livres7", type=navigation_Parcourir_les_livres_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Rechercher_un_livre_Visiteur: BinaryAssociation = BinaryAssociation(
    name="Rechercher_un_livre_Visiteur",
    ends={
        Property(name="visiteur8", type=Visiteur_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="rechercher_un_livre9", type=navigation_Rechercher_un_livre_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Visiteur_Consulter_l_aide: BinaryAssociation = BinaryAssociation(
    name="Visiteur_Consulter_l_aide",
    ends={
        Property(name="consulter_l_aide10", type=information_Consulter_l_aide_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="visiteur11", type=Visiteur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Client_Commande: BinaryAssociation = BinaryAssociation(
    name="Client_Commande",
    ends={
        Property(name="commande12", type=be_jebouquine_entities_Commande, multiplicity=Multiplicity(0, 9999)),
        Property(name="client13", type=be_jebouquine_entities_Client, multiplicity=Multiplicity(1, 1))
    }
)
LigneCommande_Livre: BinaryAssociation = BinaryAssociation(
    name="LigneCommande_Livre",
    ends={
        Property(name="livre14", type=be_jebouquine_entities_Livre, multiplicity=Multiplicity(1, 1)),
        Property(name="ligneCommande15", type=be_jebouquine_entities_LigneCommande, multiplicity=Multiplicity(0, 9999))
    }
)
Livre_Editeur: BinaryAssociation = BinaryAssociation(
    name="Livre_Editeur",
    ends={
        Property(name="editeur16", type=be_jebouquine_entities_Editeur, multiplicity=Multiplicity(1, 1)),
        Property(name="livre17", type=be_jebouquine_entities_Livre, multiplicity=Multiplicity(0, 1))
    }
)
Livre_Auteur: BinaryAssociation = BinaryAssociation(
    name="Livre_Auteur",
    ends={
        Property(name="auteur18", type=be_jebouquine_entities_Auteur, multiplicity=Multiplicity(1, 9999)),
        Property(name="livre19", type=be_jebouquine_entities_Livre, multiplicity=Multiplicity(0, 1))
    }
)
Livre_Categorie: BinaryAssociation = BinaryAssociation(
    name="Livre_Categorie",
    ends={
        Property(name="categorie20", type=be_jebouquine_entities_Categorie, multiplicity=Multiplicity(1, 9999)),
        Property(name="livre21", type=be_jebouquine_entities_Livre, multiplicity=Multiplicity(0, 1))
    }
)
Client_Commentaire: BinaryAssociation = BinaryAssociation(
    name="Client_Commentaire",
    ends={
        Property(name="commentaire22", type=be_jebouquine_entities_Commentaire, multiplicity=Multiplicity(0, 9999)),
        Property(name="client23", type=be_jebouquine_entities_Client, multiplicity=Multiplicity(1, 1))
    }
)
Commande_EtatCommande: BinaryAssociation = BinaryAssociation(
    name="Commande_EtatCommande",
    ends={
        Property(name="etatCommande24", type=be_jebouquine_entities_EtatCommande, multiplicity=Multiplicity(1, 1)),
        Property(name="commande25", type=be_jebouquine_entities_Commande, multiplicity=Multiplicity(0, 9999))
    }
)
Langue_Livre: BinaryAssociation = BinaryAssociation(
    name="Langue_Livre",
    ends={
        Property(name="livre26", type=be_jebouquine_entities_Livre, multiplicity=Multiplicity(0, 9999)),
        Property(name="langue27", type=be_jebouquine_entities_Langue, multiplicity=Multiplicity(1, 1))
    }
)
Livre_Commentaire: BinaryAssociation = BinaryAssociation(
    name="Livre_Commentaire",
    ends={
        Property(name="commentaire28", type=be_jebouquine_entities_Commentaire, multiplicity=Multiplicity(0, 9999)),
        Property(name="livre29", type=be_jebouquine_entities_Livre, multiplicity=Multiplicity(1, 1))
    }
)
Visiteur_Gerer_panier: BinaryAssociation = BinaryAssociation(
    name="Visiteur_Gerer_panier",
    ends={
        Property(name="gerer_panier30", type=panier_Gerer_panier_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="visiteur31", type=Visiteur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Commande_LigneCommande: BinaryAssociation = BinaryAssociation(
    name="Commande_LigneCommande",
    ends={
        Property(name="ligneCommande32", type=be_jebouquine_entities_LigneCommande, multiplicity=Multiplicity(1, 9999)),
        Property(name="commande33", type=be_jebouquine_entities_Commande, multiplicity=Multiplicity(1, 1))
    }
)
Commande_LivraisonInfo: BinaryAssociation = BinaryAssociation(
    name="Commande_LivraisonInfo",
    ends={
        Property(name="livraisonInfo34", type=be_jebouquine_entities_LivraisonType, multiplicity=Multiplicity(1, 1)),
        Property(name="commande35", type=be_jebouquine_entities_Commande, multiplicity=Multiplicity(0, 9999))
    }
)
Rechercher_un_livre_Recherche_par_critere: BinaryAssociation = BinaryAssociation(
    name="Rechercher_un_livre_Recherche_par_critere",
    ends={
        Property(name="recherche_par_critere36", type=navigation_Recherche_par_critere_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="rechercher_un_livre37", type=navigation_Rechercher_un_livre_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Parcourir_les_livres_Afficher_la_liste_des_livres: BinaryAssociation = BinaryAssociation(
    name="Parcourir_les_livres_Afficher_la_liste_des_livres",
    ends={
        Property(name="afficher_la_liste_des_livres38", type=navigation_Afficher_la_liste_des_livres_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="parcourir_les_livres39", type=navigation_Parcourir_les_livres_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Rechercher_un_livre_Afficher_la_liste_des_livres: BinaryAssociation = BinaryAssociation(
    name="Rechercher_un_livre_Afficher_la_liste_des_livres",
    ends={
        Property(name="afficher_la_liste_des_livres40", type=navigation_Afficher_la_liste_des_livres_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="rechercher_un_livre41", type=navigation_Rechercher_un_livre_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Administrateur_S_authentifier: BinaryAssociation = BinaryAssociation(
    name="Administrateur_S_authentifier",
    ends={
        Property(name="s_authentifier0", type=backoffice_S_authentifier_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrateur1", type=Administrateur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Systeme_Paiement_Payer_commande: BinaryAssociation = BinaryAssociation(
    name="Systeme_Paiement_Payer_commande",
    ends={
        Property(name="payer_commande2", type=commande_Payer_commande_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="systeme_Paiement3", type=Systeme_Paiement_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_3641a1a7_8c0f_4632_b29e_d1ffde2b26cb",
    types={commande_Suivre_commande_UseCase, commande_Annuler_commande_UseCase, navigation_Parcourir_les_livres_UseCase, navigation_Rechercher_un_livre_UseCase, panier_Ajouter_au_panier_UseCase, panier_Supprimer_du_panier_UseCase, panier_Gerer_panier_UseCase, panier_Modifier_quantite_livre_UseCase, panier_Passer_une_commande_UseCase, information_Consulter_l_aide_UseCase, navigation_Recherche_par_critere_UseCase, navigation_Afficher_la_liste_des_livres_UseCase, be_jebouquine_entities_Client, be_jebouquine_entities_Administrateur, be_jebouquine_entities_Livre, be_jebouquine_entities_Auteur, be_jebouquine_entities_Editeur, be_jebouquine_entities_Categorie, be_jebouquine_entities_Commande, be_jebouquine_entities_EtatCommande, be_jebouquine_entities_LivraisonType, be_jebouquine_entities_LigneCommande, be_jebouquine_entities_Langue, be_jebouquine_entities_Commentaire, backoffice_Gerer_les_produits_UseCase, backoffice_S_authentifier_UseCase, backoffice_Gerer_les_categories_UseCase, backoffice_Valider_les_commentaires_UseCase, backoffice_Gerer_les_editeurs_UseCase, backoffice_Gerer_les_auteurs_UseCase, System_Component, Client, Collection_Commande_, Collection_Commentaire_, Collection_Livre_, Collection_LigneCommande_, be_jebouquine_bo_EditeurBO, be_jebouquine_bo_AuteurBO, be_jebouquine_bo_LivreBO, be_jebouquine_bo_LigneCommandeBO, be_jebouquine_bo_CategorieBO, be_jebouquine_bo_LangueBO, be_jebouquine_bo_LivraisonTypeBO, be_jebouquine_bo_CommandeBO, be_jebouquine_bo_CommentaireBO, be_jebouquine_bo_PanierBO, be_jebouquine_bo_EtatCommandeBO, be_jebouquine_bo_ClientBO, be_jebouquine_bo_AdministrateurBO, be_jebouquine_bo_ICommandeBORemote_Interface, be_jebouquine_bo_ILangueBORemote_Interface, be_jebouquine_bo_IClientBORemote_Interface, be_jebouquine_bo_ICommentaireBORemote_Interface, be_jebouquine_bo_IEditeurBORemote_Interface, be_jebouquine_bo_ILivreBORemote_Interface, be_jebouquine_bo_IAuteurBORemote_Interface, be_jebouquine_bo_IPanierBORemote_Interface, be_jebouquine_bo_LivraisonTypeBORemote_Interface, be_jebouquine_bo_IAdministrateurBORemote_Interface, be_jebouquine_bo_LigneCommandeBORemote_Interface, be_jebouquine_bo_IEtatCommandeRemote_Interface, be_jebouquine_bo_ICategorieBORemote_Interface, Collection_Client_, Object, Collection_Object_, be_jebouquine_dao_AbstractFactory, be_jebouquine_dao_AdministrateurDAO, be_jebouquine_dao_AuteurDAO, be_jebouquine_dao_LangueDAO, be_jebouquine_dao_EditeurDAO, be_jebouquine_dao_LivreDAO, be_jebouquine_dao_LivraisonInfoDAO, be_jebouquine_dao_CategorieDAO, be_jebouquine_dao_CommentaireDAO, be_jebouquine_dao_LigneCommandeDAO, be_jebouquine_dao_ClientDAO, be_jebouquine_dao_CommandeDAO, be_jebouquine_dao_EtatCommandeDAO, Client_Actor, Visiteur_Actor, Administrateur_Actor, Systeme_Paiement_Actor, compte_Gerer_le_compte_UseCase, compte_Ajouter_commentaire_UseCase, compte_S_authentifier_UseCase, compte_Gerer_Commande_UseCase, commande_Creer_commande_UseCase, commande_Payer_commande_UseCase},
    associations={Client_S_authentifier, Parcourir_les_livres_Visiteur, Rechercher_un_livre_Visiteur, Visiteur_Consulter_l_aide, Client_Commande, LigneCommande_Livre, Livre_Editeur, Livre_Auteur, Livre_Categorie, Client_Commentaire, Commande_EtatCommande, Langue_Livre, Livre_Commentaire, Visiteur_Gerer_panier, Commande_LigneCommande, Commande_LivraisonInfo, Rechercher_un_livre_Recherche_par_critere, Parcourir_les_livres_Afficher_la_liste_des_livres, Rechercher_un_livre_Afficher_la_liste_des_livres, Administrateur_S_authentifier, Systeme_Paiement_Payer_commande},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)