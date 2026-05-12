





import java.util.List;
import java.util.ArrayList;

public class Utilisateur1  {

    private int age;
    private String nom;
    private String adresse;



    public Utilisateur1(
        int age,        String nom,        String adresse    ) {
        this.age = age;
        this.nom = nom;
        this.adresse = adresse;
    }


    public int getAge() {
        return age;
    }

    public void setAge(int age) {
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


}