





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_System_Account  {

    private String ID;
    private String Closed;
    private String Open;
    private boolean is_closed;
    private String billing_address;





    private Online_Shopping_System_Customer online_shopping_system_customer;


    public Online_Shopping_System_Account(
        String ID,        String Closed,        String Open,        boolean is_closed,        String billing_address    ) {
        this.ID = ID;
        this.Closed = Closed;
        this.Open = Open;
        this.is_closed = is_closed;
        this.billing_address = billing_address;
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
    public String getBilling_address() {
        return billing_address;
    }

    public void setBilling_address(String billing_address) {
        this.billing_address = billing_address;
    }

    public Online_Shopping_System_Customer getOnline_shopping_system_customer() {
        return online_shopping_system_customer;
    }

    public void setOnline_shopping_system_customer(Online_Shopping_System_Customer online_shopping_system_customer) {
        this.online_shopping_system_customer = online_shopping_system_customer;
    }

}