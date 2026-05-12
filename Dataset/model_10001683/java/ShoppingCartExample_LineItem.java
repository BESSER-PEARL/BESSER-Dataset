





import java.util.List;
import java.util.ArrayList;

public class ShoppingCartExample_LineItem  {

    private int price;
    private int quantity;



    public ShoppingCartExample_LineItem(
        int price,        int quantity    ) {
        this.price = price;
        this.quantity = quantity;
    }


    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }


}