





import java.util.List;
import java.util.ArrayList;

public class Transfer_Money  {

    private String ACC_NO;
    private int amount;



    public Transfer_Money(
        String ACC_NO,        int amount    ) {
        this.ACC_NO = ACC_NO;
        this.amount = amount;
    }


    public String getAcc_no() {
        return ACC_NO;
    }

    public void setAcc_no(String ACC_NO) {
        this.ACC_NO = ACC_NO;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }


}