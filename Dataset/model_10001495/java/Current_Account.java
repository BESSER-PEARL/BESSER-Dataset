





import java.util.List;
import java.util.ArrayList;

public class Current_Account  {

    private String Balance;
    private String Acc_no;



    public Current_Account(
        String Balance,        String Acc_no    ) {
        this.Balance = Balance;
        this.Acc_no = Acc_no;
    }


    public String getBalance() {
        return Balance;
    }

    public void setBalance(String Balance) {
        this.Balance = Balance;
    }
    public String getAcc_no() {
        return Acc_no;
    }

    public void setAcc_no(String Acc_no) {
        this.Acc_no = Acc_no;
    }


}