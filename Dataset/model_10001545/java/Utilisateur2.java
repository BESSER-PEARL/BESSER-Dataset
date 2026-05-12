





import java.util.List;
import java.util.ArrayList;

public class Utilisateur2  {

    private String adresse;
    private String nom;
    private int age;
    private String photoDeProfil;



    public Utilisateur2(
        String adresse,        String nom,        int age,        String photoDeProfil    ) {
        this.adresse = adresse;
        this.nom = nom;
        this.age = age;
        this.photoDeProfil = photoDeProfil;
    }


    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getPhotodeprofil() {
        return photoDeProfil;
    }

    public void setPhotodeprofil(String photoDeProfil) {
        this.photoDeProfil = photoDeProfil;
    }


}