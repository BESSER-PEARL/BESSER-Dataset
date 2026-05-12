





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_System_Account  {

    private String Open;
    private String billing_address;
    private String ID;
    private boolean is_closed;
    private String Closed;





    private List<Online_Shopping_System_Order> online_shopping_system_orders;




    private Online_Shopping_System_Customer online_shopping_system_customer;


    public Online_Shopping_System_Account(
        String Open,        String billing_address,        String ID,        boolean is_closed,        String Closed    ) {
        this.Open = Open;
        this.billing_address = billing_address;
        this.ID = ID;
        this.is_closed = is_closed;
        this.Closed = Closed;
        this.online_shopping_system_orders = new ArrayList<>();
    }

    public Online_Shopping_System_Account(
        String Open,        String billing_address,        String ID,        boolean is_closed,        String Closed        ArrayList<Online_Shopping_System_Order> online_shopping_system_orders    ) {
        this.Open = Open;
        this.billing_address = billing_address;
        this.ID = ID;
        this.is_closed = is_closed;
        this.Closed = Closed;
        this.online_shopping_system_orders = online_shopping_system_orders;
    }

    public String getOpen() {
        return Open;
    }

    public void setOpen(String Open) {
        this.Open = Open;
    }
    public String getBilling_address() {
        return billing_address;
    }

    public void setBilling_address(String billing_address) {
        this.billing_address = billing_address;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public boolean getIs_closed() {
        return is_closed;
    }

    public void setIs_closed(boolean is_closed) {
        this.is_closed = is_closed;
    }
    public String getClosed() {
        return Closed;
    }

    public void setClosed(String Closed) {
        this.Closed = Closed;
    }

    public List<Online_Shopping_System_Order> getOnline_shopping_system_orders() {
        return online_shopping_system_orders;
    }

    public void addOnline_shopping_system_order(Online_shopping_system_order online_shopping_system_order) {
        this.online_shopping_system_orders.add(online_shopping_system_order);
    }
    public Online_Shopping_System_Customer getOnline_shopping_system_customer() {
        return online_shopping_system_customer;
    }

    public void setOnline_shopping_system_customer(Online_Shopping_System_Customer online_shopping_system_customer) {
        this.online_shopping_system_customer = online_shopping_system_customer;
    }

}