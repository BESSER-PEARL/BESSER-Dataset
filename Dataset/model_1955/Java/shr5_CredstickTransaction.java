





import java.util.List;
import java.util.ArrayList;

public class shr5_CredstickTransaction  {

    private String date;
    private String amount;
    private String description;





    private shr5_Credstick shr5_credstick;


    public shr5_CredstickTransaction(
        String date,        String amount,        String description    ) {
        this.date = date;
        this.amount = amount;
        this.description = description;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public shr5_Credstick getShr5_credstick() {
        return shr5_credstick;
    }

    public void setShr5_credstick(shr5_Credstick shr5_credstick) {
        this.shr5_credstick = shr5_credstick;
    }

}