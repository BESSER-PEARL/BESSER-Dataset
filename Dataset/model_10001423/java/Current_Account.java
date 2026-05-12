





import java.util.List;
import java.util.ArrayList;

public class Current_Account  {

    private String Balance;
    private String AccountNumber;



    public Current_Account(
        String Balance,        String AccountNumber    ) {
        this.Balance = Balance;
        this.AccountNumber = AccountNumber;
    }


    public String getBalance() {
        return Balance;
    }

    public void setBalance(String Balance) {
        this.Balance = Balance;
    }
    public String getAccountnumber() {
        return AccountNumber;
    }

    public void setAccountnumber(String AccountNumber) {
        this.AccountNumber = AccountNumber;
    }


}