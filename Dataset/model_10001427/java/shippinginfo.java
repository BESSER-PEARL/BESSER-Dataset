




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class shippinginfo  {

    private String shipping_Address;
    private int shipping_cost;
    private LocalDate shipping_date;
    private String shipping_id;
    private String shipping_type;





    private order order;


    public shippinginfo(
        String shipping_Address,        int shipping_cost,        LocalDate shipping_date,        String shipping_id,        String shipping_type    ) {
        this.shipping_Address = shipping_Address;
        this.shipping_cost = shipping_cost;
        this.shipping_date = shipping_date;
        this.shipping_id = shipping_id;
        this.shipping_type = shipping_type;
    }


    public String getShipping_address() {
        return shipping_Address;
    }

    public void setShipping_address(String shipping_Address) {
        this.shipping_Address = shipping_Address;
    }
    public int getShipping_cost() {
        return shipping_cost;
    }

    public void setShipping_cost(int shipping_cost) {
        this.shipping_cost = shipping_cost;
    }
    public LocalDate getShipping_date() {
        return shipping_date;
    }

    public void setShipping_date(LocalDate shipping_date) {
        this.shipping_date = shipping_date;
    }
    public String getShipping_id() {
        return shipping_id;
    }

    public void setShipping_id(String shipping_id) {
        this.shipping_id = shipping_id;
    }
    public String getShipping_type() {
        return shipping_type;
    }

    public void setShipping_type(String shipping_type) {
        this.shipping_type = shipping_type;
    }

    public order getOrder() {
        return order;
    }

    public void setOrder(order order) {
        this.order = order;
    }

}