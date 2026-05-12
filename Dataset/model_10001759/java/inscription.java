





import java.util.List;
import java.util.ArrayList;

public class inscription  {

    private String informations_conducteur;
    private String informations_passager;





    private administrateur administrateur;


    public inscription(
        String informations_conducteur,        String informations_passager    ) {
        this.informations_conducteur = informations_conducteur;
        this.informations_passager = informations_passager;
    }


    public String getInformations_conducteur() {
        return informations_conducteur;
    }

    public void setInformations_conducteur(String informations_conducteur) {
        this.informations_conducteur = informations_conducteur;
    }
    public String getInformations_passager() {
        return informations_passager;
    }

    public void setInformations_passager(String informations_passager) {
        this.informations_passager = informations_passager;
    }

    public administrateur getAdministrateur() {
        return administrateur;
    }

    public void setAdministrateur(administrateur administrateur) {
        this.administrateur = administrateur;
    }

}