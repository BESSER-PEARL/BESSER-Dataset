





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String Date_off;
    private int Amount;



    public Payment(
        String Date_off,        int Amount    ) {
        this.Date_off = Date_off;
        this.Amount = Amount;
    }


    public String getDate_off() {
        return Date_off;
    }

    public void setDate_off(String Date_off) {
        this.Date_off = Date_off;
    }
    public int getAmount() {
        return Amount;
    }

    public void setAmount(int Amount) {
        this.Amount = Amount;
    }


}