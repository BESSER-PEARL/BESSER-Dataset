





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String Status;
    private String CustomerID;
    private String CustomerName;
    private String DateShipped;
    private String ShippingID;
    private int OrderID;
    private String DateCreated;





    private Customer customer;


    public Order(
        String Status,        String CustomerID,        String CustomerName,        String DateShipped,        String ShippingID,        int OrderID,        String DateCreated    ) {
        this.Status = Status;
        this.CustomerID = CustomerID;
        this.CustomerName = CustomerName;
        this.DateShipped = DateShipped;
        this.ShippingID = ShippingID;
        this.OrderID = OrderID;
        this.DateCreated = DateCreated;
    }


    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }
    public String getCustomerid() {
        return CustomerID;
    }

    public void setCustomerid(String CustomerID) {
        this.CustomerID = CustomerID;
    }
    public String getCustomername() {
        return CustomerName;
    }

    public void setCustomername(String CustomerName) {
        this.CustomerName = CustomerName;
    }
    public String getDateshipped() {
        return DateShipped;
    }

    public void setDateshipped(String DateShipped) {
        this.DateShipped = DateShipped;
    }
    public String getShippingid() {
        return ShippingID;
    }

    public void setShippingid(String ShippingID) {
        this.ShippingID = ShippingID;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public String getDatecreated() {
        return DateCreated;
    }

    public void setDatecreated(String DateCreated) {
        this.DateCreated = DateCreated;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}