





import java.util.List;
import java.util.ArrayList;

public class navigation_Recherche_par_critere_UseCase  {






    private navigation_Rechercher_un_livre_UseCase navigation_rechercher_un_livre_usecase;


    public navigation_Recherche_par_critere_UseCase(
    ) {
    }



    public navigation_Rechercher_un_livre_UseCase getNavigation_rechercher_un_livre_usecase() {
        return navigation_rechercher_un_livre_usecase;
    }

    public void setNavigation_rechercher_un_livre_usecase(navigation_Rechercher_un_livre_UseCase navigation_rechercher_un_livre_usecase) {
        this.navigation_rechercher_un_livre_usecase = navigation_rechercher_un_livre_usecase;
    }

}