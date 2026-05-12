





import java.util.List;
import java.util.ArrayList;

public class Savings_Account  {

    private String AccountNumber;
    private String Balance;





    private Current_Account current_account;


    public Savings_Account(
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

    public Current_Account getCurrent_account() {
        return current_account;
    }

    public void setCurrent_account(Current_Account current_account) {
        this.current_account = current_account;
    }

}