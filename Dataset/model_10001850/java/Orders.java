





import java.util.List;
import java.util.ArrayList;

public class Orders  {

    private int orderId;
    private String status;
    private String shippingId;
    private String dateCreated;
    private String customerId;
    private String dateShipped;
    private String customerName;





    private shippingInfo shippinginfo;




    private Customer customer;




    private Order_Details order_details;


    public Orders(
        int orderId,        String status,        String shippingId,        String dateCreated,        String customerId,        String dateShipped,        String customerName    ) {
        this.orderId = orderId;
        this.status = status;
        this.shippingId = shippingId;
        this.dateCreated = dateCreated;
        this.customerId = customerId;
        this.dateShipped = dateShipped;
        this.customerName = customerName;
    }


    public int getOrderid() {
        return orderId;
    }

    public void setOrderid(int orderId) {
        this.orderId = orderId;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getShippingid() {
        return shippingId;
    }

    public void setShippingid(String shippingId) {
        this.shippingId = shippingId;
    }
    public String getDatecreated() {
        return dateCreated;
    }

    public void setDatecreated(String dateCreated) {
        this.dateCreated = dateCreated;
    }
    public String getCustomerid() {
        return customerId;
    }

    public void setCustomerid(String customerId) {
        this.customerId = customerId;
    }
    public String getDateshipped() {
        return dateShipped;
    }

    public void setDateshipped(String dateShipped) {
        this.dateShipped = dateShipped;
    }
    public String getCustomername() {
        return customerName;
    }

    public void setCustomername(String customerName) {
        this.customerName = customerName;
    }

    public shippingInfo getShippinginfo() {
        return shippinginfo;
    }

    public void setShippinginfo(shippingInfo shippinginfo) {
        this.shippinginfo = shippinginfo;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public Order_Details getOrder_details() {
        return order_details;
    }

    public void setOrder_details(Order_Details order_details) {
        this.order_details = order_details;
    }

}