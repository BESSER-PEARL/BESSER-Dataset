





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String datedeliver;
    private String shippingid;
    private String status;
    private String dateorder;
    private String orderid;
    private String customerid;



    public Order(
        String datedeliver,        String shippingid,        String status,        String dateorder,        String orderid,        String customerid    ) {
        this.datedeliver = datedeliver;
        this.shippingid = shippingid;
        this.status = status;
        this.dateorder = dateorder;
        this.orderid = orderid;
        this.customerid = customerid;
    }


    public String getDatedeliver() {
        return datedeliver;
    }

    public void setDatedeliver(String datedeliver) {
        this.datedeliver = datedeliver;
    }
    public String getShippingid() {
        return shippingid;
    }

    public void setShippingid(String shippingid) {
        this.shippingid = shippingid;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getDateorder() {
        return dateorder;
    }

    public void setDateorder(String dateorder) {
        this.dateorder = dateorder;
    }
    public String getOrderid() {
        return orderid;
    }

    public void setOrderid(String orderid) {
        this.orderid = orderid;
    }
    public String getCustomerid() {
        return customerid;
    }

    public void setCustomerid(String customerid) {
        this.customerid = customerid;
    }


}