





import java.util.List;
import java.util.ArrayList;

public class Client  {

    private String fonction;
    private String nom;



    public Client(
        String fonction,        String nom    ) {
        this.fonction = fonction;
        this.nom = nom;
    }


    public String getFonction() {
        return fonction;
    }

    public void setFonction(String fonction) {
        this.fonction = fonction;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }


}