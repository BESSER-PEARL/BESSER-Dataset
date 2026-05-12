





import java.util.List;
import java.util.ArrayList;

public class order  {

    private int orderId;
    private String shippingid;
    private int customerid;
    private String name;
    private String datecreated;





    private orderDetail orderdetail;




    private coustomer coustomer;


    public order(
        int orderId,        String shippingid,        int customerid,        String name,        String datecreated    ) {
        this.orderId = orderId;
        this.shippingid = shippingid;
        this.customerid = customerid;
        this.name = name;
        this.datecreated = datecreated;
    }


    public int getOrderid() {
        return orderId;
    }

    public void setOrderid(int orderId) {
        this.orderId = orderId;
    }
    public String getShippingid() {
        return shippingid;
    }

    public void setShippingid(String shippingid) {
        this.shippingid = shippingid;
    }
    public int getCustomerid() {
        return customerid;
    }

    public void setCustomerid(int customerid) {
        this.customerid = customerid;
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