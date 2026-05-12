





import java.util.List;
import java.util.ArrayList;

public class Visiteur_Actor  {






    private information_Consulter_l_aide_UseCase information_consulter_l_aide_usecase;




    private panier_Gerer_panier_UseCase panier_gerer_panier_usecase;




    private navigation_Rechercher_un_livre_UseCase navigation_rechercher_un_livre_usecase;




    private navigation_Parcourir_les_livres_UseCase navigation_parcourir_les_livres_usecase;


    public Visiteur_Actor(
    ) {
    }



    public information_Consulter_l_aide_UseCase getInformation_consulter_l_aide_usecase() {
        return information_consulter_l_aide_usecase;
    }

    public void setInformation_consulter_l_aide_usecase(information_Consulter_l_aide_UseCase information_consulter_l_aide_usecase) {
        this.information_consulter_l_aide_usecase = information_consulter_l_aide_usecase;
    }
    public panier_Gerer_panier_UseCase getPanier_gerer_panier_usecase() {
        return panier_gerer_panier_usecase;
    }

    public void setPanier_gerer_panier_usecase(panier_Gerer_panier_UseCase panier_gerer_panier_usecase) {
        this.panier_gerer_panier_usecase = panier_gerer_panier_usecase;
    }
    public navigation_Rechercher_un_livre_UseCase getNavigation_rechercher_un_livre_usecase() {
        return navigation_rechercher_un_livre_usecase;
    }

    public void setNavigation_rechercher_un_livre_usecase(navigation_Rechercher_un_livre_UseCase navigation_rechercher_un_livre_usecase) {
        this.navigation_rechercher_un_livre_usecase = navigation_rechercher_un_livre_usecase;
    }
    public navigation_Parcourir_les_livres_UseCase getNavigation_parcourir_les_livres_usecase() {
        return navigation_parcourir_les_livres_usecase;
    }

    public void setNavigation_parcourir_les_livres_usecase(navigation_Parcourir_les_livres_UseCase navigation_parcourir_les_livres_usecase) {
        this.navigation_parcourir_les_livres_usecase = navigation_parcourir_les_livres_usecase;
    }

}