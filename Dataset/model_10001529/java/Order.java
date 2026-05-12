





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int id;
    private int quantity;
    private String orderDate;
    private String orderStatus;





    private Product product;


    public Order(
        int id,        int quantity,        String orderDate,        String orderStatus    ) {
        this.id = id;
        this.quantity = quantity;
        this.orderDate = orderDate;
        this.orderStatus = orderStatus;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public String getOrderdate() {
        return orderDate;
    }

    public void setOrderdate(String orderDate) {
        this.orderDate = orderDate;
    }
    public String getOrderstatus() {
        return orderStatus;
    }

    public void setOrderstatus(String orderStatus) {
        this.orderStatus = orderStatus;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}