





import java.util.List;
import java.util.ArrayList;

public class Produit  {

    private String posologie;
    private int id;
    private String nom;
    private String dose;





    private Ordonance ordonance;


    public Produit(
        String posologie,        int id,        String nom,        String dose    ) {
        this.posologie = posologie;
        this.id = id;
        this.nom = nom;
        this.dose = dose;
    }


    public String getPosologie() {
        return posologie;
    }

    public void setPosologie(String posologie) {
        this.posologie = posologie;
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
    public String getDose() {
        return dose;
    }

    public void setDose(String dose) {
        this.dose = dose;
    }

    public Ordonance getOrdonance() {
        return ordonance;
    }

    public void setOrdonance(Ordonance ordonance) {
        this.ordonance = ordonance;
    }

}