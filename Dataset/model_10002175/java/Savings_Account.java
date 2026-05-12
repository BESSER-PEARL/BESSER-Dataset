





import java.util.List;
import java.util.ArrayList;

public class Savings_Account  {

    private int balance;
    private String accountNumber;



    public Savings_Account(
        int balance,        String accountNumber    ) {
        this.balance = balance;
        this.accountNumber = accountNumber;
    }


    public int getBalance() {
        return balance;
    }

    public void setBalance(int balance) {
        this.balance = balance;
    }
    public String getAccountnumber() {
        return accountNumber;
    }

    public void setAccountnumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }


}