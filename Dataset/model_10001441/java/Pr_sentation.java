





import java.util.List;
import java.util.ArrayList;

public class Pr_sentation  {

    private String adresse;
    private String ouverture;
    private String description;
    private String siteDeCommande;
    private String numTel;





    private FicheRestaurant ficherestaurant;


    public Pr_sentation(
        String adresse,        String ouverture,        String description,        String siteDeCommande,        String numTel    ) {
        this.adresse = adresse;
        this.ouverture = ouverture;
        this.description = description;
        this.siteDeCommande = siteDeCommande;
        this.numTel = numTel;
    }


    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }
    public String getOuverture() {
        return ouverture;
    }

    public void setOuverture(String ouverture) {
        this.ouverture = ouverture;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getSitedecommande() {
        return siteDeCommande;
    }

    public void setSitedecommande(String siteDeCommande) {
        this.siteDeCommande = siteDeCommande;
    }
    public String getNumtel() {
        return numTel;
    }

    public void setNumtel(String numTel) {
        this.numTel = numTel;
    }

    public FicheRestaurant getFicherestaurant() {
        return ficherestaurant;
    }

    public void setFicherestaurant(FicheRestaurant ficherestaurant) {
        this.ficherestaurant = ficherestaurant;
    }

}