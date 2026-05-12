





import java.util.List;
import java.util.ArrayList;

public class LineItem  {

    private float price;
    private int quantity;





    private ConNguoi connguoi;




    private Order order;


    public LineItem(
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

    public ConNguoi getConnguoi() {
        return connguoi;
    }

    public void setConnguoi(ConNguoi connguoi) {
        this.connguoi = connguoi;
    }
    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}