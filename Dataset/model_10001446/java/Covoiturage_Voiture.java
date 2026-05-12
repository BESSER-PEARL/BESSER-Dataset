





import java.util.List;
import java.util.ArrayList;

public class Covoiturage_Voiture  {

    private int id;
    private String confort;
    private String categorie;
    private int nbPlaces;
    private String marque;
    private String model;
    private String attribute;



    public Covoiturage_Voiture(
        int id,        String confort,        String categorie,        int nbPlaces,        String marque,        String model,        String attribute    ) {
        this.id = id;
        this.confort = confort;
        this.categorie = categorie;
        this.nbPlaces = nbPlaces;
        this.marque = marque;
        this.model = model;
        this.attribute = attribute;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getConfort() {
        return confort;
    }

    public void setConfort(String confort) {
        this.confort = confort;
    }
    public String getCategorie() {
        return categorie;
    }

    public void setCategorie(String categorie) {
        this.categorie = categorie;
    }
    public int getNbplaces() {
        return nbPlaces;
    }

    public void setNbplaces(int nbPlaces) {
        this.nbPlaces = nbPlaces;
    }
    public String getMarque() {
        return marque;
    }

    public void setMarque(String marque) {
        this.marque = marque;
    }
    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}