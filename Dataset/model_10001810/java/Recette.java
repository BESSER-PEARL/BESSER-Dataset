





import java.util.List;
import java.util.ArrayList;

public class Recette  {

    private int produit_id;
    private int id;



    public Recette(
        int produit_id,        int id    ) {
        this.produit_id = produit_id;
        this.id = id;
    }


    public int getProduit_id() {
        return produit_id;
    }

    public void setProduit_id(int produit_id) {
        this.produit_id = produit_id;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}