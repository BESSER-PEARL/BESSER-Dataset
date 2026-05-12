





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int OrderID;
    private String DateShipped;
    private String CustomerName;
    private String CustomerID;
    private String DateCreated;
    private String ShippingID;
    private String Status;





    private Customer customer;


    public Order(
        int OrderID,        String DateShipped,        String CustomerName,        String CustomerID,        String DateCreated,        String ShippingID,        String Status    ) {
        this.OrderID = OrderID;
        this.DateShipped = DateShipped;
        this.CustomerName = CustomerName;
        this.CustomerID = CustomerID;
        this.DateCreated = DateCreated;
        this.ShippingID = ShippingID;
        this.Status = Status;
    }


    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public String getDateshipped() {
        return DateShipped;
    }

    public void setDateshipped(String DateShipped) {
        this.DateShipped = DateShipped;
    }
    public String getCustomername() {
        return CustomerName;
    }

    public void setCustomername(String CustomerName) {
        this.CustomerName = CustomerName;
    }
    public String getCustomerid() {
        return CustomerID;
    }

    public void setCustomerid(String CustomerID) {
        this.CustomerID = CustomerID;
    }
    public String getDatecreated() {
        return DateCreated;
    }

    public void setDatecreated(String DateCreated) {
        this.DateCreated = DateCreated;
    }
    public String getShippingid() {
        return ShippingID;
    }

    public void setShippingid(String ShippingID) {
        this.ShippingID = ShippingID;
    }
    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}