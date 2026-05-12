





import java.util.List;
import java.util.ArrayList;

public class Content  {

    private float price;
    private int quantity;





    private Customer customer;


    public Content(
        float price,        int quantity    ) {
        this.price = price;
        this.quantity = quantity;
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

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}