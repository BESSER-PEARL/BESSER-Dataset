





import java.util.List;
import java.util.ArrayList;

public class libsys_UnpaidFee  {

    private int amount;
    private String reason;



    public libsys_UnpaidFee(
        int amount,        String reason    ) {
        this.amount = amount;
        this.reason = reason;
    }


    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }


}