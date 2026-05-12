





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_System_Account  {

    private String billing_address;
    private String Open;
    private boolean is_closed;
    private String ID;
    private String Closed;





    private Online_Shopping_System_Customer online_shopping_system_customer;


    public Online_Shopping_System_Account(
        String billing_address,        String Open,        boolean is_closed,        String ID,        String Closed    ) {
        this.billing_address = billing_address;
        this.Open = Open;
        this.is_closed = is_closed;
        this.ID = ID;
        this.Closed = Closed;
    }


    public String getBilling_address() {
        return billing_address;
    }

    public void setBilling_address(String billing_address) {
        this.billing_address = billing_address;
    }
    public String getOpen() {
        return Open;
    }

    public void setOpen(String Open) {
        this.Open = Open;
    }
    public boolean getIs_closed() {
        return is_closed;
    }

    public void setIs_closed(boolean is_closed) {
        this.is_closed = is_closed;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getClosed() {
        return Closed;
    }

    public void setClosed(String Closed) {
        this.Closed = Closed;
    }

    public Online_Shopping_System_Customer getOnline_shopping_system_customer() {
        return online_shopping_system_customer;
    }

    public void setOnline_shopping_system_customer(Online_Shopping_System_Customer online_shopping_system_customer) {
        this.online_shopping_system_customer = online_shopping_system_customer;
    }

}