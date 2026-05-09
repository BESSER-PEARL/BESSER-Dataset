





import java.util.List;
import java.util.ArrayList;

public class tda593_billing_Purchase  {

    private int id;
    private float price;
    private int quantity;



    public tda593_billing_Purchase(
        int id,        float price,        int quantity    ) {
        this.id = id;
        this.price = price;
        this.quantity = quantity;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }


}