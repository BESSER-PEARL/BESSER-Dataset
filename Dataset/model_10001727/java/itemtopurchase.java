





import java.util.List;
import java.util.ArrayList;

public class itemtopurchase  {

    private int quantity;
    private int itemtopurchase;





    private shoppingcart shoppingcart;


    public itemtopurchase(
        int quantity,        int itemtopurchase    ) {
        this.quantity = quantity;
        this.itemtopurchase = itemtopurchase;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public int getItemtopurchase() {
        return itemtopurchase;
    }

    public void setItemtopurchase(int itemtopurchase) {
        this.itemtopurchase = itemtopurchase;
    }

    public shoppingcart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(shoppingcart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}