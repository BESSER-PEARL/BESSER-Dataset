





import java.util.List;
import java.util.ArrayList;

public class LineItem  {

    private int quantity;
    private float price;





    private List<Order> orders;




    private ShoppingCart shoppingcart;


    public LineItem(
        int quantity,        float price    ) {
        this.quantity = quantity;
        this.price = price;
        this.orders = new ArrayList<>();
    }

    public LineItem(
        int quantity,        float price        ArrayList<Order> orders    ) {
        this.quantity = quantity;
        this.price = price;
        this.orders = orders;
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

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}