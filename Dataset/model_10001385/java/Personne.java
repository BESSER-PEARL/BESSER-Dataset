





import java.util.List;
import java.util.ArrayList;

public class Personne  {

    private String prenom;
    private String nom;
    private String adresse;
    private String dateNaissance;
    private String telPrive;
    private String email;



    public Personne(
        String prenom,        String nom,        String adresse,        String dateNaissance,        String telPrive,        String email    ) {
        this.prenom = prenom;
        this.nom = nom;
        this.adresse = adresse;
        this.dateNaissance = dateNaissance;
        this.telPrive = telPrive;
        this.email = email;
    }


    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }
    public String getDatenaissance() {
        return dateNaissance;
    }

    public void setDatenaissance(String dateNaissance) {
        this.dateNaissance = dateNaissance;
    }
    public String getTelprive() {
        return telPrive;
    }

    public void setTelprive(String telPrive) {
        this.telPrive = telPrive;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}