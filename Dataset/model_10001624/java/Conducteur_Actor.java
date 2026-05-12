





import java.util.List;
import java.util.ArrayList;

public class Conducteur_Actor  {






    private Proposition_de_voyage_UseCase proposition_de_voyage_usecase;




    private S_enregistre_UseCase s_enregistre_usecase;


    public Conducteur_Actor(
    ) {
    }



    public Proposition_de_voyage_UseCase getProposition_de_voyage_usecase() {
        return proposition_de_voyage_usecase;
    }

    public void setProposition_de_voyage_usecase(Proposition_de_voyage_UseCase proposition_de_voyage_usecase) {
        this.proposition_de_voyage_usecase = proposition_de_voyage_usecase;
    }
    public S_enregistre_UseCase getS_enregistre_usecase() {
        return s_enregistre_usecase;
    }

    public void setS_enregistre_usecase(S_enregistre_UseCase s_enregistre_usecase) {
        this.s_enregistre_usecase = s_enregistre_usecase;
    }

}