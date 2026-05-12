





import java.util.List;
import java.util.ArrayList;

public class LineItem  {

    private float price;
    private int quantity;





    private List<Order> orders;




    private ShoppingCart shoppingcart;


    public LineItem(
        float price,        int quantity    ) {
        this.price = price;
        this.quantity = quantity;
        this.orders = new ArrayList<>();
    }

    public LineItem(
        float price,        int quantity        ArrayList<Order> orders    ) {
        this.price = price;
        this.quantity = quantity;
        this.orders = orders;
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