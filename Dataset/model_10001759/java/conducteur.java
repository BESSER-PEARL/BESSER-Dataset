





import java.util.List;
import java.util.ArrayList;

public class conducteur  {

    private String informations_conducteur;





    private inscription inscription;


    public conducteur(
        String informations_conducteur    ) {
        this.informations_conducteur = informations_conducteur;
    }


    public String getInformations_conducteur() {
        return informations_conducteur;
    }

    public void setInformations_conducteur(String informations_conducteur) {
        this.informations_conducteur = informations_conducteur;
    }

    public inscription getInscription() {
        return inscription;
    }

    public void setInscription(inscription inscription) {
        this.inscription = inscription;
    }

}