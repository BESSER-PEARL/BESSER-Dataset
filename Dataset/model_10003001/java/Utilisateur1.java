





import java.util.List;
import java.util.ArrayList;

public class Utilisateur1  {

    private String nom;
    private String adresse;
    private int age;



    public Utilisateur1(
        String nom,        String adresse,        int age    ) {
        this.nom = nom;
        this.adresse = adresse;
        this.age = age;
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
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }


}