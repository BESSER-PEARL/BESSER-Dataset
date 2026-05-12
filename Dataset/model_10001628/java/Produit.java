





import java.util.List;
import java.util.ArrayList;

public class Produit  {

    private String posologie;
    private String dose;
    private int id;
    private String nom;





    private Ordonance ordonance;


    public Produit(
        String posologie,        String dose,        int id,        String nom    ) {
        this.posologie = posologie;
        this.dose = dose;
        this.id = id;
        this.nom = nom;
    }


    public String getPosologie() {
        return posologie;
    }

    public void setPosologie(String posologie) {
        this.posologie = posologie;
    }
    public String getDose() {
        return dose;
    }

    public void setDose(String dose) {
        this.dose = dose;
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

    public Ordonance getOrdonance() {
        return ordonance;
    }

    public void setOrdonance(Ordonance ordonance) {
        this.ordonance = ordonance;
    }

}