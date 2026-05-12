





import java.util.List;
import java.util.ArrayList;

public class Personne  {

    private String prenom;
    private int id;
    private String nom;



    public Personne(
        String prenom,        int id,        String nom    ) {
        this.prenom = prenom;
        this.id = id;
        this.nom = nom;
    }


    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }


}