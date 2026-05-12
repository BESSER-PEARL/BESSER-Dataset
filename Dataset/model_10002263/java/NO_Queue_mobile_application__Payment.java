





import java.util.List;
import java.util.ArrayList;

public class NO_Queue_mobile_application__Payment  {

    private String Paid;
    private String Details;
    private String Total;
    private String ID;





    private NO_Queue_mobile_application__Account no_queue_mobile_application__account;


    public NO_Queue_mobile_application__Payment(
        String Paid,        String Details,        String Total,        String ID    ) {
        this.Paid = Paid;
        this.Details = Details;
        this.Total = Total;
        this.ID = ID;
    }


    public String getPaid() {
        return Paid;
    }

    public void setPaid(String Paid) {
        this.Paid = Paid;
    }
    public String getDetails() {
        return Details;
    }

    public void setDetails(String Details) {
        this.Details = Details;
    }
    public String getTotal() {
        return Total;
    }

    public void setTotal(String Total) {
        this.Total = Total;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public NO_Queue_mobile_application__Account getNo_queue_mobile_application__account() {
        return no_queue_mobile_application__account;
    }

    public void setNo_queue_mobile_application__account(NO_Queue_mobile_application__Account no_queue_mobile_application__account) {
        this.no_queue_mobile_application__account = no_queue_mobile_application__account;
    }

}