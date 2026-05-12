





import java.util.List;
import java.util.ArrayList;

public class Current_Account  {

    private int Balance;
    private int AccountNumber;



    public Current_Account(
        int Balance,        int AccountNumber    ) {
        this.Balance = Balance;
        this.AccountNumber = AccountNumber;
    }


    public int getBalance() {
        return Balance;
    }

    public void setBalance(int Balance) {
        this.Balance = Balance;
    }
    public int getAccountnumber() {
        return AccountNumber;
    }

    public void setAccountnumber(int AccountNumber) {
        this.AccountNumber = AccountNumber;
    }


}