





import java.util.List;
import java.util.ArrayList;

public class Current_Account  {

    private String AccountNumber;
    private String Balance;



    public Current_Account(
        String AccountNumber,        String Balance    ) {
        this.AccountNumber = AccountNumber;
        this.Balance = Balance;
    }


    public String getAccountnumber() {
        return AccountNumber;
    }

    public void setAccountnumber(String AccountNumber) {
        this.AccountNumber = AccountNumber;
    }
    public String getBalance() {
        return Balance;
    }

    public void setBalance(String Balance) {
        this.Balance = Balance;
    }


}