





import java.util.List;
import java.util.ArrayList;

public class Order_Sent  {

    private String Item_id;
    private String sentOrder_id;
    private String quantity;
    private String order_status;





    private List<Administrator> administrators;


    public Order_Sent(
        String Item_id,        String sentOrder_id,        String quantity,        String order_status    ) {
        this.Item_id = Item_id;
        this.sentOrder_id = sentOrder_id;
        this.quantity = quantity;
        this.order_status = order_status;
        this.administrators = new ArrayList<>();
    }

    public Order_Sent(
        String Item_id,        String sentOrder_id,        String quantity,        String order_status        ArrayList<Administrator> administrators    ) {
        this.Item_id = Item_id;
        this.sentOrder_id = sentOrder_id;
        this.quantity = quantity;
        this.order_status = order_status;
        this.administrators = administrators;
    }

    public String getItem_id() {
        return Item_id;
    }

    public void setItem_id(String Item_id) {
        this.Item_id = Item_id;
    }
    public String getSentorder_id() {
        return sentOrder_id;
    }

    public void setSentorder_id(String sentOrder_id) {
        this.sentOrder_id = sentOrder_id;
    }
    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }
    public String getOrder_status() {
        return order_status;
    }

    public void setOrder_status(String order_status) {
        this.order_status = order_status;
    }

    public List<Administrator> getAdministrators() {
        return administrators;
    }

    public void addAdministrator(Administrator administrator) {
        this.administrators.add(administrator);
    }

}