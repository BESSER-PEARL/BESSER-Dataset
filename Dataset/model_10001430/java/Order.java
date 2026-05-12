





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String creationDate;
    private String dateShipped;
    private float totalPrice;
    private int shippingId;
    private None status;
    private int orderId;
    private int customerId;





    private Customer customer;


    public Order(
        String creationDate,        String dateShipped,        float totalPrice,        int shippingId,        None status,        int orderId,        int customerId    ) {
        this.creationDate = creationDate;
        this.dateShipped = dateShipped;
        this.totalPrice = totalPrice;
        this.shippingId = shippingId;
        this.status = status;
        this.orderId = orderId;
        this.customerId = customerId;
    }


    public String getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(String creationDate) {
        this.creationDate = creationDate;
    }
    public String getDateshipped() {
        return dateShipped;
    }

    public void setDateshipped(String dateShipped) {
        this.dateShipped = dateShipped;
    }
    public float getTotalprice() {
        return totalPrice;
    }

    public void setTotalprice(float totalPrice) {
        this.totalPrice = totalPrice;
    }
    public int getShippingid() {
        return shippingId;
    }

    public void setShippingid(int shippingId) {
        this.shippingId = shippingId;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public int getOrderid() {
        return orderId;
    }

    public void setOrderid(int orderId) {
        this.orderId = orderId;
    }
    public int getCustomerid() {
        return customerId;
    }

    public void setCustomerid(int customerId) {
        this.customerId = customerId;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}