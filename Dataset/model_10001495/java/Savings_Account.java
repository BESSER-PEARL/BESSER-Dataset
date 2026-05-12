





import java.util.List;
import java.util.ArrayList;

public class Savings_Account  {

    private String Acc_no;
    private String Balance;



    public Savings_Account(
        String Acc_no,        String Balance    ) {
        this.Acc_no = Acc_no;
        this.Balance = Balance;
    }


    public String getAcc_no() {
        return Acc_no;
    }

    public void setAcc_no(String Acc_no) {
        this.Acc_no = Acc_no;
    }
    public String getBalance() {
        return Balance;
    }

    public void setBalance(String Balance) {
        this.Balance = Balance;
    }


}