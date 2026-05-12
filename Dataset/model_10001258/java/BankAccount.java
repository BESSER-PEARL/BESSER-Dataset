





import java.util.List;
import java.util.ArrayList;

public class BankAccount  {

    private float balance;
    private String accountHolder;
    private int accountNumber;





    private Bank bank;


    public BankAccount(
        float balance,        String accountHolder,        int accountNumber    ) {
        this.balance = balance;
        this.accountHolder = accountHolder;
        this.accountNumber = accountNumber;
    }


    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }
    public String getAccountholder() {
        return accountHolder;
    }

    public void setAccountholder(String accountHolder) {
        this.accountHolder = accountHolder;
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