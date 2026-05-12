





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String orderStatus;
    private String orderDate;
    private int id;
    private int quantity;





    private Product product;


    public Order(
        String orderStatus,        String orderDate,        int id,        int quantity    ) {
        this.orderStatus = orderStatus;
        this.orderDate = orderDate;
        this.id = id;
        this.quantity = quantity;
    }


    public String getOrderstatus() {
        return orderStatus;
    }

    public void setOrderstatus(String orderStatus) {
        this.orderStatus = orderStatus;
    }
    public String getOrderdate() {
        return orderDate;
    }

    public void setOrderdate(String orderDate) {
        this.orderDate = orderDate;
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

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}