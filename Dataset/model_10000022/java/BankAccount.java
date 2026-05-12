





import java.util.List;
import java.util.ArrayList;

public class BankAccount  {

    private String balance;
    private String owner;



    public BankAccount(
        String balance,        String owner    ) {
        this.balance = balance;
        this.owner = owner;
    }


    public String getBalance() {
        return balance;
    }

    public void setBalance(String balance) {
        this.balance = balance;
    }
    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }


}