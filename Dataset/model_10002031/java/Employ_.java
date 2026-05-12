





import java.util.List;
import java.util.ArrayList;

public class Employ_  {

    private String prenom;
    private String poste;
    private String adresse;
    private String nom;
    private int ID;



    public Employ_(
        String prenom,        String poste,        String adresse,        String nom,        int ID    ) {
        this.prenom = prenom;
        this.poste = poste;
        this.adresse = adresse;
        this.nom = nom;
        this.ID = ID;
    }


    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }
    public String getPoste() {
        return poste;
    }

    public void setPoste(String poste) {
        this.poste = poste;
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
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }


}