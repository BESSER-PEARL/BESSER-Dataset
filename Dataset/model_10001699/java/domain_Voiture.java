





import java.util.List;
import java.util.ArrayList;

public class domain_Voiture  {

    private int nbPlaces;
    private String categorie;
    private int id;
    private String model;
    private String marque;
    private String confort;





    private domain_Profil domain_profil;


    public domain_Voiture(
        int nbPlaces,        String categorie,        int id,        String model,        String marque,        String confort    ) {
        this.nbPlaces = nbPlaces;
        this.categorie = categorie;
        this.id = id;
        this.model = model;
        this.marque = marque;
        this.confort = confort;
    }


    public int getNbplaces() {
        return nbPlaces;
    }

    public void setNbplaces(int nbPlaces) {
        this.nbPlaces = nbPlaces;
    }
    public String getCategorie() {
        return categorie;
    }

    public void setCategorie(String categorie) {
        this.categorie = categorie;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }
    public String getMarque() {
        return marque;
    }

    public void setMarque(String marque) {
        this.marque = marque;
    }
    public String getConfort() {
        return confort;
    }

    public void setConfort(String confort) {
        this.confort = confort;
    }

    public domain_Profil getDomain_profil() {
        return domain_profil;
    }

    public void setDomain_profil(domain_Profil domain_profil) {
        this.domain_profil = domain_profil;
    }

}