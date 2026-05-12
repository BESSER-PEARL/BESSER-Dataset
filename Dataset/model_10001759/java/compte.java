





import java.util.List;
import java.util.ArrayList;

public class compte  {

    private String informations_passager;
    private String informations_conducteur;



    public compte(
        String informations_passager,        String informations_conducteur    ) {
        this.informations_passager = informations_passager;
        this.informations_conducteur = informations_conducteur;
    }


    public String getInformations_passager() {
        return informations_passager;
    }

    public void setInformations_passager(String informations_passager) {
        this.informations_passager = informations_passager;
    }
    public String getInformations_conducteur() {
        return informations_conducteur;
    }

    public void setInformations_conducteur(String informations_conducteur) {
        this.informations_conducteur = informations_conducteur;
    }


}