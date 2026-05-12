





import java.util.List;
import java.util.ArrayList;

public class LineItem  {

    private int quantity;
    private float price;





    private Cosul_de_cumparaturi cosul_de_cumparaturi;




    private Ordin ordin;


    public LineItem(
        int quantity,        float price    ) {
        this.quantity = quantity;
        this.price = price;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public Cosul_de_cumparaturi getCosul_de_cumparaturi() {
        return cosul_de_cumparaturi;
    }

    public void setCosul_de_cumparaturi(Cosul_de_cumparaturi cosul_de_cumparaturi) {
        this.cosul_de_cumparaturi = cosul_de_cumparaturi;
    }
    public Ordin getOrdin() {
        return ordin;
    }

    public void setOrdin(Ordin ordin) {
        this.ordin = ordin;
    }

}