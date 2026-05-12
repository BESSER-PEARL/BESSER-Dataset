





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String customerid;
    private String dateorder;
    private String shippingid;
    private String datedeliver;
    private String orderid;
    private String status;



    public Order(
        String customerid,        String dateorder,        String shippingid,        String datedeliver,        String orderid,        String status    ) {
        this.customerid = customerid;
        this.dateorder = dateorder;
        this.shippingid = shippingid;
        this.datedeliver = datedeliver;
        this.orderid = orderid;
        this.status = status;
    }


    public String getCustomerid() {
        return customerid;
    }

    public void setCustomerid(String customerid) {
        this.customerid = customerid;
    }
    public String getDateorder() {
        return dateorder;
    }

    public void setDateorder(String dateorder) {
        this.dateorder = dateorder;
    }
    public String getShippingid() {
        return shippingid;
    }

    public void setShippingid(String shippingid) {
        this.shippingid = shippingid;
    }
    public String getDatedeliver() {
        return datedeliver;
    }

    public void setDatedeliver(String datedeliver) {
        this.datedeliver = datedeliver;
    }
    public String getOrderid() {
        return orderid;
    }

    public void setOrderid(String orderid) {
        this.orderid = orderid;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}