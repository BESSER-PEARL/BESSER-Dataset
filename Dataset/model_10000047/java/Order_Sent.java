





import java.util.List;
import java.util.ArrayList;

public class Order_Sent  {

    private String sentOrder_id;
    private String order_status;
    private String Item_id;
    private String quantity;





    private List<Administrator> administrators;


    public Order_Sent(
        String sentOrder_id,        String order_status,        String Item_id,        String quantity    ) {
        this.sentOrder_id = sentOrder_id;
        this.order_status = order_status;
        this.Item_id = Item_id;
        this.quantity = quantity;
        this.administrators = new ArrayList<>();
    }

    public Order_Sent(
        String sentOrder_id,        String order_status,        String Item_id,        String quantity        ArrayList<Administrator> administrators    ) {
        this.sentOrder_id = sentOrder_id;
        this.order_status = order_status;
        this.Item_id = Item_id;
        this.quantity = quantity;
        this.administrators = administrators;
    }

    public String getSentorder_id() {
        return sentOrder_id;
    }

    public void setSentorder_id(String sentOrder_id) {
        this.sentOrder_id = sentOrder_id;
    }
    public String getOrder_status() {
        return order_status;
    }

    public void setOrder_status(String order_status) {
        this.order_status = order_status;
    }
    public String getItem_id() {
        return Item_id;
    }

    public void setItem_id(String Item_id) {
        this.Item_id = Item_id;
    }
    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }

    public List<Administrator> getAdministrators() {
        return administrators;
    }

    public void addAdministrator(Administrator administrator) {
        this.administrators.add(administrator);
    }

}