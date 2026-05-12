





import java.util.List;
import java.util.ArrayList;

public class Utilisateur2  {

    private String adresse;
    private int age;
    private int nbAvis;
    private String nom;
    private String photoDeProfil;



    public Utilisateur2(
        String adresse,        int age,        int nbAvis,        String nom,        String photoDeProfil    ) {
        this.adresse = adresse;
        this.age = age;
        this.nbAvis = nbAvis;
        this.nom = nom;
        this.photoDeProfil = photoDeProfil;
    }


    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public int getNbavis() {
        return nbAvis;
    }

    public void setNbavis(int nbAvis) {
        this.nbAvis = nbAvis;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public String getPhotodeprofil() {
        return photoDeProfil;
    }

    public void setPhotodeprofil(String photoDeProfil) {
        this.photoDeProfil = photoDeProfil;
    }


}