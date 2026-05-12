





import java.util.List;
import java.util.ArrayList;

public class order  {

    private int customerid;
    private int orderId;
    private String name;
    private String datecreated;
    private String shippingid;





    private orderDetail orderdetail;




    private coustomer coustomer;


    public order(
        int customerid,        int orderId,        String name,        String datecreated,        String shippingid    ) {
        this.customerid = customerid;
        this.orderId = orderId;
        this.name = name;
        this.datecreated = datecreated;
        this.shippingid = shippingid;
    }


    public int getCustomerid() {
        return customerid;
    }

    public void setCustomerid(int customerid) {
        this.customerid = customerid;
    }
    public int getOrderid() {
        return orderId;
    }

    public void setOrderid(int orderId) {
        this.orderId = orderId;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDatecreated() {
        return datecreated;
    }

    public void setDatecreated(String datecreated) {
        this.datecreated = datecreated;
    }
    public String getShippingid() {
        return shippingid;
    }

    public void setShippingid(String shippingid) {
        this.shippingid = shippingid;
    }

    public orderDetail getOrderdetail() {
        return orderdetail;
    }

    public void setOrderdetail(orderDetail orderdetail) {
        this.orderdetail = orderdetail;
    }
    public coustomer getCoustomer() {
        return coustomer;
    }

    public void setCoustomer(coustomer coustomer) {
        this.coustomer = coustomer;
    }

}