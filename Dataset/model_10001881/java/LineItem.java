





import java.util.List;
import java.util.ArrayList;

public class LineItem  {

    private float price;
    private int quantity;





    private ShoppinCart shoppincart;




    private List<Order_Compute_Price> order_compute_prices;


    public LineItem(
        float price,        int quantity    ) {
        this.price = price;
        this.quantity = quantity;
        this.order_compute_prices = new ArrayList<>();
    }

    public LineItem(
        float price,        int quantity        ArrayList<Order_Compute_Price> order_compute_prices    ) {
        this.price = price;
        this.quantity = quantity;
        this.order_compute_prices = order_compute_prices;
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

    public ShoppinCart getShoppincart() {
        return shoppincart;
    }

    public void setShoppincart(ShoppinCart shoppincart) {
        this.shoppincart = shoppincart;
    }
    public List<Order_Compute_Price> getOrder_compute_prices() {
        return order_compute_prices;
    }

    public void addOrder_compute_price(Order_compute_price order_compute_price) {
        this.order_compute_prices.add(order_compute_price);
    }

}