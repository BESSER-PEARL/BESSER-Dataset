





import java.util.List;
import java.util.ArrayList;

public class Amount  {

    private String Subvention_date;
    private int Month;
    private int Amount;



    public Amount(
        String Subvention_date,        int Month,        int Amount    ) {
        this.Subvention_date = Subvention_date;
        this.Month = Month;
        this.Amount = Amount;
    }


    public String getSubvention_date() {
        return Subvention_date;
    }

    public void setSubvention_date(String Subvention_date) {
        this.Subvention_date = Subvention_date;
    }
    public int getMonth() {
        return Month;
    }

    public void setMonth(int Month) {
        this.Month = Month;
    }
    public int getAmount() {
        return Amount;
    }

    public void setAmount(int Amount) {
        this.Amount = Amount;
    }


}