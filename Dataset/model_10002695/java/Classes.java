





import java.util.List;
import java.util.ArrayList;

public class Classes  {

    private String Name;
    private String quantity;





    private Order order;




    private ShoppingCart shoppingcart;


    public Classes(
        String Name,        String quantity    ) {
        this.Name = Name;
        this.quantity = quantity;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}