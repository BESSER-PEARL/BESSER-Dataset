





import java.util.List;
import java.util.ArrayList;

public class Personne  {

    private String nom;
    private String numero;
    private String prenom;
    private int numeroMedecin;
    private String attribute;
    private int id;



    public Personne(
        String nom,        String numero,        String prenom,        int numeroMedecin,        String attribute,        int id    ) {
        this.nom = nom;
        this.numero = numero;
        this.prenom = prenom;
        this.numeroMedecin = numeroMedecin;
        this.attribute = attribute;
        this.id = id;
    }


    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }
    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }
    public int getNumeromedecin() {
        return numeroMedecin;
    }

    public void setNumeromedecin(int numeroMedecin) {
        this.numeroMedecin = numeroMedecin;
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


}