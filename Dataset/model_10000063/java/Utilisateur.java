





import java.util.List;
import java.util.ArrayList;

public class Utilisateur  {

    private String nom;
    private String nom3;
    private String nom4;
    private String prenom;



    public Utilisateur(
        String nom,        String nom3,        String nom4,        String prenom    ) {
        this.nom = nom;
        this.nom3 = nom3;
        this.nom4 = nom4;
        this.prenom = prenom;
    }


    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public String getNom3() {
        return nom3;
    }

    public void setNom3(String nom3) {
        this.nom3 = nom3;
    }
    public String getNom4() {
        return nom4;
    }

    public void setNom4(String nom4) {
        this.nom4 = nom4;
    }
    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }


}