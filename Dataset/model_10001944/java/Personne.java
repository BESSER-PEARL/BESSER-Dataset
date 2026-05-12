





import java.util.List;
import java.util.ArrayList;

public class Personne  {

    private String dateNaissance;
    private String prenom;
    private String adresse;
    private String telephone;
    private int id;
    private String lieuNaissance;
    private int numeroCIN;
    private String nom;
    private String email;



    public Personne(
        String dateNaissance,        String prenom,        String adresse,        String telephone,        int id,        String lieuNaissance,        int numeroCIN,        String nom,        String email    ) {
        this.dateNaissance = dateNaissance;
        this.prenom = prenom;
        this.adresse = adresse;
        this.telephone = telephone;
        this.id = id;
        this.lieuNaissance = lieuNaissance;
        this.numeroCIN = numeroCIN;
        this.nom = nom;
        this.email = email;
    }


    public String getDatenaissance() {
        return dateNaissance;
    }

    public void setDatenaissance(String dateNaissance) {
        this.dateNaissance = dateNaissance;
    }
    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }
    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }
    public String getTelephone() {
        return telephone;
    }

    public void setTelephone(String telephone) {
        this.telephone = telephone;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getLieunaissance() {
        return lieuNaissance;
    }

    public void setLieunaissance(String lieuNaissance) {
        this.lieuNaissance = lieuNaissance;
    }
    public int getNumerocin() {
        return numeroCIN;
    }

    public void setNumerocin(int numeroCIN) {
        this.numeroCIN = numeroCIN;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}