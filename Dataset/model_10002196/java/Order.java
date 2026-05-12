





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int OrderID;
    private String dateShipped;
    private String dateCreated;
    private String customerID;
    private String status;
    private String shippingID;





    private Customer customer;


    public Order(
        int OrderID,        String dateShipped,        String dateCreated,        String customerID,        String status,        String shippingID    ) {
        this.OrderID = OrderID;
        this.dateShipped = dateShipped;
        this.dateCreated = dateCreated;
        this.customerID = customerID;
        this.status = status;
        this.shippingID = shippingID;
    }


    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public String getDateshipped() {
        return dateShipped;
    }

    public void setDateshipped(String dateShipped) {
        this.dateShipped = dateShipped;
    }
    public String getDatecreated() {
        return dateCreated;
    }

    public void setDatecreated(String dateCreated) {
        this.dateCreated = dateCreated;
    }
    public String getCustomerid() {
        return customerID;
    }

    public void setCustomerid(String customerID) {
        this.customerID = customerID;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getShippingid() {
        return shippingID;
    }

    public void setShippingid(String shippingID) {
        this.shippingID = shippingID;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}