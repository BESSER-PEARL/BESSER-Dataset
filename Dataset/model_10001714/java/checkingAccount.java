





import java.util.List;
import java.util.ArrayList;

public class checkingAccount  {

    private int accountNo;
    private int noOfTransactions;



    public checkingAccount(
        int accountNo,        int noOfTransactions    ) {
        this.accountNo = accountNo;
        this.noOfTransactions = noOfTransactions;
    }


    public int getAccountno() {
        return accountNo;
    }

    public void setAccountno(int accountNo) {
        this.accountNo = accountNo;
    }
    public int getNooftransactions() {
        return noOfTransactions;
    }

    public void setNooftransactions(int noOfTransactions) {
        this.noOfTransactions = noOfTransactions;
    }


}