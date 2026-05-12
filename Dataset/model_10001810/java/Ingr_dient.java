





import java.util.List;
import java.util.ArrayList;

public class Ingr_dient  {

    private String unit_;
    private String poids;
    private String nom;
    private int id;





    private Stock stock;


    public Ingr_dient(
        String unit_,        String poids,        String nom,        int id    ) {
        this.unit_ = unit_;
        this.poids = poids;
        this.nom = nom;
        this.id = id;
    }


    public String getUnit_() {
        return unit_;
    }

    public void setUnit_(String unit_) {
        this.unit_ = unit_;
    }
    public String getPoids() {
        return poids;
    }

    public void setPoids(String poids) {
        this.poids = poids;
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

    public Stock getStock() {
        return stock;
    }

    public void setStock(Stock stock) {
        this.stock = stock;
    }

}