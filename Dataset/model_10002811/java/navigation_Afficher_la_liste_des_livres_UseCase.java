





import java.util.List;
import java.util.ArrayList;

public class navigation_Afficher_la_liste_des_livres_UseCase  {






    private navigation_Rechercher_un_livre_UseCase navigation_rechercher_un_livre_usecase;




    private navigation_Parcourir_les_livres_UseCase navigation_parcourir_les_livres_usecase;


    public navigation_Afficher_la_liste_des_livres_UseCase(
    ) {
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