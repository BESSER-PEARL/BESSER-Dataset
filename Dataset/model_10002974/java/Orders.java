





import java.util.List;
import java.util.ArrayList;

public class Orders  {

    private String CustomerId;
    private int OrderId;
    private String status;
    private String Date;
    private String dateCreated;
    private String ShippingId;
    private String customerName;





    private Client client;




    private Shipping_Info shipping_info;


    public Orders(
        String CustomerId,        int OrderId,        String status,        String Date,        String dateCreated,        String ShippingId,        String customerName    ) {
        this.CustomerId = CustomerId;
        this.OrderId = OrderId;
        this.status = status;
        this.Date = Date;
        this.dateCreated = dateCreated;
        this.ShippingId = ShippingId;
        this.customerName = customerName;
    }


    public String getCustomerid() {
        return CustomerId;
    }

    public void setCustomerid(String CustomerId) {
        this.CustomerId = CustomerId;
    }
    public int getOrderid() {
        return OrderId;
    }

    public void setOrderid(int OrderId) {
        this.OrderId = OrderId;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public String getDatecreated() {
        return dateCreated;
    }

    public void setDatecreated(String dateCreated) {
        this.dateCreated = dateCreated;
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

    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }
    public Shipping_Info getShipping_info() {
        return shipping_info;
    }

    public void setShipping_info(Shipping_Info shipping_info) {
        this.shipping_info = shipping_info;
    }

}