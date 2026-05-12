





import java.util.List;
import java.util.ArrayList;

public class Cat_gorie  {

    private String nom;
    private int id;



    public Cat_gorie(
        String nom,        int id    ) {
        this.nom = nom;
        this.id = id;
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


}