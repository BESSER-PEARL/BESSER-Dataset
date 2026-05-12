





import java.util.List;
import java.util.ArrayList;

public class BankAccount  {

    private String ownerName;
    private float balance;
    private String attribute;



    public BankAccount(
        String ownerName,        float balance,        String attribute    ) {
        this.ownerName = ownerName;
        this.balance = balance;
        this.attribute = attribute;
    }


    public String getOwnername() {
        return ownerName;
    }

    public void setOwnername(String ownerName) {
        this.ownerName = ownerName;
    }
    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}