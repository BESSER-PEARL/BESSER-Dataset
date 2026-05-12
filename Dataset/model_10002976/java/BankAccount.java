





import java.util.List;
import java.util.ArrayList;

public class BankAccount  {

    private float balance;
    private int accountNumber;
    private String accountHolder;





    private Bank bank;


    public BankAccount(
        float balance,        int accountNumber,        String accountHolder    ) {
        this.balance = balance;
        this.accountNumber = accountNumber;
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
    public String getAccountholder() {
        return accountHolder;
    }

    public void setAccountholder(String accountHolder) {
        this.accountHolder = accountHolder;
    }

    public Bank getBank() {
        return bank;
    }

    public void setBank(Bank bank) {
        this.bank = bank;
    }

}