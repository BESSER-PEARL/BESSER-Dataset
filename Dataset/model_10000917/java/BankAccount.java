





import java.util.List;
import java.util.ArrayList;

public class BankAccount  {

    private String accountHolder;
    private float balance;
    private int accountNumber;





    private Bank bank;


    public BankAccount(
        String accountHolder,        float balance,        int accountNumber    ) {
        this.accountHolder = accountHolder;
        this.balance = balance;
        this.accountNumber = accountNumber;
    }


    public String getAccountholder() {
        return accountHolder;
    }

    public void setAccountholder(String accountHolder) {
        this.accountHolder = accountHolder;
    }
    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }
    public int getAccountnumber() {
        return accountNumber;
    }

    public void setAccountnumber(int accountNumber) {
        this.accountNumber = accountNumber;
    }

    public Bank getBank() {
        return bank;
    }

    public void setBank(Bank bank) {
        this.bank = bank;
    }

}