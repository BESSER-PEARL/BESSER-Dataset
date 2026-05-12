





import java.util.List;
import java.util.ArrayList;

public class commande_Payer_commande_UseCase  {






    private Systeme_Paiement_Actor systeme_paiement_actor;


    public commande_Payer_commande_UseCase(
    ) {
    }



    public Systeme_Paiement_Actor getSysteme_paiement_actor() {
        return systeme_paiement_actor;
    }

    public void setSysteme_paiement_actor(Systeme_Paiement_Actor systeme_paiement_actor) {
        this.systeme_paiement_actor = systeme_paiement_actor;
    }

}