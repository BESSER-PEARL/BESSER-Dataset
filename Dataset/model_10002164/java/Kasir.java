





import java.util.List;
import java.util.ArrayList;

public class Kasir  {

    private String order_id;
    private String cust_id;



    public Kasir(
        String order_id,        String cust_id    ) {
        this.order_id = order_id;
        this.cust_id = cust_id;
    }


    public String getOrder_id() {
        return order_id;
    }

    public void setOrder_id(String order_id) {
        this.order_id = order_id;
    }
    public String getCust_id() {
        return cust_id;
    }

    public void setCust_id(String cust_id) {
        this.cust_id = cust_id;
    }


}