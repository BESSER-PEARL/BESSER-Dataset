





import java.util.List;
import java.util.ArrayList;

public class Savings_Account  {

    private int Balance;
    private int AccountNumber;





    private Current_Account current_account;


    public Savings_Account(
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

    public Current_Account getCurrent_account() {
        return current_account;
    }

    public void setCurrent_account(Current_Account current_account) {
        this.current_account = current_account;
    }

}