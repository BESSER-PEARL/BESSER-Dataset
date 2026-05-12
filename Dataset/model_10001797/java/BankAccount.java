





import java.util.List;
import java.util.ArrayList;

public class BankAccount  {

    private float balance;
    private String accountHolderName;



    public BankAccount(
        float balance,        String accountHolderName    ) {
        this.balance = balance;
        this.accountHolderName = accountHolderName;
    }


    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }
    public String getAccountholdername() {
        return accountHolderName;
    }

    public void setAccountholdername(String accountHolderName) {
        this.accountHolderName = accountHolderName;
    }


}