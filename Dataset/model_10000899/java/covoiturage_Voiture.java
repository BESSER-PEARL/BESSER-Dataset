





import java.util.List;
import java.util.ArrayList;

public class covoiturage_Voiture  {

    private String couleur;
    private String model;
    private int id;
    private boolean climatiseur;
    private String confort;
    private String categorie;
    private boolean tabac;
    private int nbPlaces;
    private String marque;





    private covoiturage_Personne covoiturage_personne;


    public covoiturage_Voiture(
        String couleur,        String model,        int id,        boolean climatiseur,        String confort,        String categorie,        boolean tabac,        int nbPlaces,        String marque    ) {
        this.couleur = couleur;
        this.model = model;
        this.id = id;
        this.climatiseur = climatiseur;
        this.confort = confort;
        this.categorie = categorie;
        this.tabac = tabac;
        this.nbPlaces = nbPlaces;
        this.marque = marque;
    }


    public String getCouleur() {
        return couleur;
    }

    public void setCouleur(String couleur) {
        this.couleur = couleur;
    }
    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public boolean getClimatiseur() {
        return climatiseur;
    }

    public void setClimatiseur(boolean climatiseur) {
        this.climatiseur = climatiseur;
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
    public boolean getTabac() {
        return tabac;
    }

    public void setTabac(boolean tabac) {
        this.tabac = tabac;
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

    public covoiturage_Personne getCovoiturage_personne() {
        return covoiturage_personne;
    }

    public void setCovoiturage_personne(covoiturage_Personne covoiturage_personne) {
        this.covoiturage_personne = covoiturage_personne;
    }

}