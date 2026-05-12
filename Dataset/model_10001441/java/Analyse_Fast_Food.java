





import java.util.List;
import java.util.ArrayList;

public class Analyse_Fast_Food  {

    private String notes;
    private int prixMin;
    private String nom;
    private String Ville;
    private String numeroTel;
    private String Adresse;
    private String proprietaire;
    private int nbPlaces;
    private String photos;
    private int prixMax;
    private String horaires;



    public Analyse_Fast_Food(
        String notes,        int prixMin,        String nom,        String Ville,        String numeroTel,        String Adresse,        String proprietaire,        int nbPlaces,        String photos,        int prixMax,        String horaires    ) {
        this.notes = notes;
        this.prixMin = prixMin;
        this.nom = nom;
        this.Ville = Ville;
        this.numeroTel = numeroTel;
        this.Adresse = Adresse;
        this.proprietaire = proprietaire;
        this.nbPlaces = nbPlaces;
        this.photos = photos;
        this.prixMax = prixMax;
        this.horaires = horaires;
    }


    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
    public int getPrixmin() {
        return prixMin;
    }

    public void setPrixmin(int prixMin) {
        this.prixMin = prixMin;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public String getVille() {
        return Ville;
    }

    public void setVille(String Ville) {
        this.Ville = Ville;
    }
    public String getNumerotel() {
        return numeroTel;
    }

    public void setNumerotel(String numeroTel) {
        this.numeroTel = numeroTel;
    }
    public String getAdresse() {
        return Adresse;
    }

    public void setAdresse(String Adresse) {
        this.Adresse = Adresse;
    }
    public String getProprietaire() {
        return proprietaire;
    }

    public void setProprietaire(String proprietaire) {
        this.proprietaire = proprietaire;
    }
    public int getNbplaces() {
        return nbPlaces;
    }

    public void setNbplaces(int nbPlaces) {
        this.nbPlaces = nbPlaces;
    }
    public String getPhotos() {
        return photos;
    }

    public void setPhotos(String photos) {
        this.photos = photos;
    }
    public int getPrixmax() {
        return prixMax;
    }

    public void setPrixmax(int prixMax) {
        this.prixMax = prixMax;
    }
    public String getHoraires() {
        return horaires;
    }

    public void setHoraires(String horaires) {
        this.horaires = horaires;
    }


}