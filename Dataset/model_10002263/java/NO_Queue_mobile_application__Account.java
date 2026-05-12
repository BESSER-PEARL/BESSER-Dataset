





import java.util.List;
import java.util.ArrayList;

public class NO_Queue_mobile_application__Account  {

    private String Open;
    private String ID;
    private String billing_address;
    private String Closed;
    private boolean is_closed;





    private NO_Queue_mobile_application__Customer no_queue_mobile_application__customer;


    public NO_Queue_mobile_application__Account(
        String Open,        String ID,        String billing_address,        String Closed,        boolean is_closed    ) {
        this.Open = Open;
        this.ID = ID;
        this.billing_address = billing_address;
        this.Closed = Closed;
        this.is_closed = is_closed;
    }


    public String getOpen() {
        return Open;
    }

    public void setOpen(String Open) {
        this.Open = Open;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getBilling_address() {
        return billing_address;
    }

    public void setBilling_address(String billing_address) {
        this.billing_address = billing_address;
    }
    public String getClosed() {
        return Closed;
    }

    public void setClosed(String Closed) {
        this.Closed = Closed;
    }
    public boolean getIs_closed() {
        return is_closed;
    }

    public void setIs_closed(boolean is_closed) {
        this.is_closed = is_closed;
    }

    public NO_Queue_mobile_application__Customer getNo_queue_mobile_application__customer() {
        return no_queue_mobile_application__customer;
    }

    public void setNo_queue_mobile_application__customer(NO_Queue_mobile_application__Customer no_queue_mobile_application__customer) {
        this.no_queue_mobile_application__customer = no_queue_mobile_application__customer;
    }

}