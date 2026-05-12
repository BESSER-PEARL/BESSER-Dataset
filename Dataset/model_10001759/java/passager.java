





import java.util.List;
import java.util.ArrayList;

public class passager  {

    private String informations_passager;





    private trajet trajet;




    private paiement paiement;




    private administrateur administrateur;




    private inscription inscription;




    private compte compte;


    public passager(
        String informations_passager    ) {
        this.informations_passager = informations_passager;
    }


    public String getInformations_passager() {
        return informations_passager;
    }

    public void setInformations_passager(String informations_passager) {
        this.informations_passager = informations_passager;
    }

    public trajet getTrajet() {
        return trajet;
    }

    public void setTrajet(trajet trajet) {
        this.trajet = trajet;
    }
    public paiement getPaiement() {
        return paiement;
    }

    public void setPaiement(paiement paiement) {
        this.paiement = paiement;
    }
    public administrateur getAdministrateur() {
        return administrateur;
    }

    public void setAdministrateur(administrateur administrateur) {
        this.administrateur = administrateur;
    }
    public inscription getInscription() {
        return inscription;
    }

    public void setInscription(inscription inscription) {
        this.inscription = inscription;
    }
    public compte getCompte() {
        return compte;
    }

    public void setCompte(compte compte) {
        this.compte = compte;
    }

}