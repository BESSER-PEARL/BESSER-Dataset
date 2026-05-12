





import java.util.List;
import java.util.ArrayList;

public class customer  {

    private String customer_name;
    private String _attr;
    private None customer_Id;



    public customer(
        String customer_name,        String _attr,        None customer_Id    ) {
        this.customer_name = customer_name;
        this._attr = _attr;
        this.customer_Id = customer_Id;
    }


    public String getCustomer_name() {
        return customer_name;
    }

    public void setCustomer_name(String customer_name) {
        this.customer_name = customer_name;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }
    public None getCustomer_id() {
        return customer_Id;
    }

    public void setCustomer_id(None customer_Id) {
        this.customer_Id = customer_Id;
    }


}