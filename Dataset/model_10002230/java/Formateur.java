





import java.util.List;
import java.util.ArrayList;

public class Formateur  {

    private String Nom;
    private String Prenom;





    private Prestation prestation;


    public Formateur(
        String Nom,        String Prenom    ) {
        this.Nom = Nom;
        this.Prenom = Prenom;
    }


    public String getNom() {
        return Nom;
    }

    public void setNom(String Nom) {
        this.Nom = Nom;
    }
    public String getPrenom() {
        return Prenom;
    }

    public void setPrenom(String Prenom) {
        this.Prenom = Prenom;
    }

    public Prestation getPrestation() {
        return prestation;
    }

    public void setPrestation(Prestation prestation) {
        this.prestation = prestation;
    }

}