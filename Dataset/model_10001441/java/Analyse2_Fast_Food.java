





import java.util.List;
import java.util.ArrayList;

public class Analyse2_Fast_Food  {

    private String Adresse;
    private String Ville;
    private int prixMax;
    private String reviews;
    private String siteDeCommande;
    private String description;
    private String nom;
    private int prixMin;
    private int nbPlaces;
    private String horaires;
    private String photos;
    private String numeroTel;
    private String proprietaire;



    public Analyse2_Fast_Food(
        String Adresse,        String Ville,        int prixMax,        String reviews,        String siteDeCommande,        String description,        String nom,        int prixMin,        int nbPlaces,        String horaires,        String photos,        String numeroTel,        String proprietaire    ) {
        this.Adresse = Adresse;
        this.Ville = Ville;
        this.prixMax = prixMax;
        this.reviews = reviews;
        this.siteDeCommande = siteDeCommande;
        this.description = description;
        this.nom = nom;
        this.prixMin = prixMin;
        this.nbPlaces = nbPlaces;
        this.horaires = horaires;
        this.photos = photos;
        this.numeroTel = numeroTel;
        this.proprietaire = proprietaire;
    }


    public String getAdresse() {
        return Adresse;
    }

    public void setAdresse(String Adresse) {
        this.Adresse = Adresse;
    }
    public String getVille() {
        return Ville;
    }

    public void setVille(String Ville) {
        this.Ville = Ville;
    }
    public int getPrixmax() {
        return prixMax;
    }

    public void setPrixmax(int prixMax) {
        this.prixMax = prixMax;
    }
    public String getReviews() {
        return reviews;
    }

    public void setReviews(String reviews) {
        this.reviews = reviews;
    }
    public String getSitedecommande() {
        return siteDeCommande;
    }

    public void setSitedecommande(String siteDeCommande) {
        this.siteDeCommande = siteDeCommande;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public int getPrixmin() {
        return prixMin;
    }

    public void setPrixmin(int prixMin) {
        this.prixMin = prixMin;
    }
    public int getNbplaces() {
        return nbPlaces;
    }

    public void setNbplaces(int nbPlaces) {
        this.nbPlaces = nbPlaces;
    }
    public String getHoraires() {
        return horaires;
    }

    public void setHoraires(String horaires) {
        this.horaires = horaires;
    }
    public String getPhotos() {
        return photos;
    }

    public void setPhotos(String photos) {
        this.photos = photos;
    }
    public String getNumerotel() {
        return numeroTel;
    }

    public void setNumerotel(String numeroTel) {
        this.numeroTel = numeroTel;
    }
    public String getProprietaire() {
        return proprietaire;
    }

    public void setProprietaire(String proprietaire) {
        this.proprietaire = proprietaire;
    }


}