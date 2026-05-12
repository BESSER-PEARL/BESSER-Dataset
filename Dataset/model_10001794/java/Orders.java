





import java.util.List;
import java.util.ArrayList;

public class Orders  {

    private String dateCreated;
    private String Date;
    private String CustomerId;
    private String status;
    private int OrderId;
    private String ShippingId;
    private String customerName;





    private Shipping_Info shipping_info;


    public Orders(
        String dateCreated,        String Date,        String CustomerId,        String status,        int OrderId,        String ShippingId,        String customerName    ) {
        this.dateCreated = dateCreated;
        this.Date = Date;
        this.CustomerId = CustomerId;
        this.status = status;
        this.OrderId = OrderId;
        this.ShippingId = ShippingId;
        this.customerName = customerName;
    }


    public String getDatecreated() {
        return dateCreated;
    }

    public void setDatecreated(String dateCreated) {
        this.dateCreated = dateCreated;
    }
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public String getCustomerid() {
        return CustomerId;
    }

    public void setCustomerid(String CustomerId) {
        this.CustomerId = CustomerId;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getOrderid() {
        return OrderId;
    }

    public void setOrderid(int OrderId) {
        this.OrderId = OrderId;
    }
    public String getShippingid() {
        return ShippingId;
    }

    public void setShippingid(String ShippingId) {
        this.ShippingId = ShippingId;
    }
    public String getCustomername() {
        return customerName;
    }

    public void setCustomername(String customerName) {
        this.customerName = customerName;
    }

    public Shipping_Info getShipping_info() {
        return shipping_info;
    }

    public void setShipping_info(Shipping_Info shipping_info) {
        this.shipping_info = shipping_info;
    }

}