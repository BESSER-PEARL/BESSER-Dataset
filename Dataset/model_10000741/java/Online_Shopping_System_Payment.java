





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_System_Payment  {

    private String Paid;
    private String Total;
    private String ID;
    private String Details;





    private Online_Shopping_System_Account online_shopping_system_account;


    public Online_Shopping_System_Payment(
        String Paid,        String Total,        String ID,        String Details    ) {
        this.Paid = Paid;
        this.Total = Total;
        this.ID = ID;
        this.Details = Details;
    }


    public String getPaid() {
        return Paid;
    }

    public void setPaid(String Paid) {
        this.Paid = Paid;
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
    public String getDetails() {
        return Details;
    }

    public void setDetails(String Details) {
        this.Details = Details;
    }

    public Online_Shopping_System_Account getOnline_shopping_system_account() {
        return online_shopping_system_account;
    }

    public void setOnline_shopping_system_account(Online_Shopping_System_Account online_shopping_system_account) {
        this.online_shopping_system_account = online_shopping_system_account;
    }

}