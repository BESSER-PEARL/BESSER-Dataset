





import java.util.List;
import java.util.ArrayList;

public class Savings_Account2  {

    private String accountNumber;
    private int balance;



    public Savings_Account2(
        String accountNumber,        int balance    ) {
        this.accountNumber = accountNumber;
        this.balance = balance;
    }


    public String getAccountnumber() {
        return accountNumber;
    }

    public void setAccountnumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }
    public int getBalance() {
        return balance;
    }

    public void setBalance(int balance) {
        this.balance = balance;
    }


}