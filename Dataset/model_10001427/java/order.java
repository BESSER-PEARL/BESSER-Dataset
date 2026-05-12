




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class order  {

    private String status;
    private String c_name;
    private String shippingid;
    private LocalDate shipping_date;
    private LocalDate date_created;
    private int order_ID;





    private orderDetail orderdetail;




    private User user;


    public order(
        String status,        String c_name,        String shippingid,        LocalDate shipping_date,        LocalDate date_created,        int order_ID    ) {
        this.status = status;
        this.c_name = c_name;
        this.shippingid = shippingid;
        this.shipping_date = shipping_date;
        this.date_created = date_created;
        this.order_ID = order_ID;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getC_name() {
        return c_name;
    }

    public void setC_name(String c_name) {
        this.c_name = c_name;
    }
    public String getShippingid() {
        return shippingid;
    }

    public void setShippingid(String shippingid) {
        this.shippingid = shippingid;
    }
    public LocalDate getShipping_date() {
        return shipping_date;
    }

    public void setShipping_date(LocalDate shipping_date) {
        this.shipping_date = shipping_date;
    }
    public LocalDate getDate_created() {
        return date_created;
    }

    public void setDate_created(LocalDate date_created) {
        this.date_created = date_created;
    }
    public int getOrder_id() {
        return order_ID;
    }

    public void setOrder_id(int order_ID) {
        this.order_ID = order_ID;
    }

    public orderDetail getOrderdetail() {
        return orderdetail;
    }

    public void setOrderdetail(orderDetail orderdetail) {
        this.orderdetail = orderdetail;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}