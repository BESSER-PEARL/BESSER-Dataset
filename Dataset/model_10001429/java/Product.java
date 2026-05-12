





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int stock;
    private String price;
    private int u_id;





    private OrderDetails orderdetails;


    public Product(
        int stock,        String price,        int u_id    ) {
        this.stock = stock;
        this.price = price;
        this.u_id = u_id;
    }


    public int getStock() {
        return stock;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public int getU_id() {
        return u_id;
    }

    public void setU_id(int u_id) {
        this.u_id = u_id;
    }

    public OrderDetails getOrderdetails() {
        return orderdetails;
    }

    public void setOrderdetails(OrderDetails orderdetails) {
        this.orderdetails = orderdetails;
    }

}