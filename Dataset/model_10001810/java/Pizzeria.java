





import java.util.List;
import java.util.ArrayList;

public class Pizzeria  {

    private String nom;
    private int id;
    private int adresse_id;





    private Utilisateur utilisateur;




    private Adresse adresse;


    public Pizzeria(
        String nom,        int id,        int adresse_id    ) {
        this.nom = nom;
        this.id = id;
        this.adresse_id = adresse_id;
    }


    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getAdresse_id() {
        return adresse_id;
    }

    public void setAdresse_id(int adresse_id) {
        this.adresse_id = adresse_id;
    }

    public Utilisateur getUtilisateur() {
        return utilisateur;
    }

    public void setUtilisateur(Utilisateur utilisateur) {
        this.utilisateur = utilisateur;
    }
    public Adresse getAdresse() {
        return adresse;
    }

    public void setAdresse(Adresse adresse) {
        this.adresse = adresse;
    }

}