





import java.util.List;
import java.util.ArrayList;

public class Personne  {

    private String nom;
    private int numeroMedecin;
    private String prenom;
    private String attribute;
    private int id;
    private String numero;



    public Personne(
        String nom,        int numeroMedecin,        String prenom,        String attribute,        int id,        String numero    ) {
        this.nom = nom;
        this.numeroMedecin = numeroMedecin;
        this.prenom = prenom;
        this.attribute = attribute;
        this.id = id;
        this.numero = numero;
    }


    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public int getNumeromedecin() {
        return numeroMedecin;
    }

    public void setNumeromedecin(int numeroMedecin) {
        this.numeroMedecin = numeroMedecin;
    }
    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }


}