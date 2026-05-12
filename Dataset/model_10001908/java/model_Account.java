





import java.util.List;
import java.util.ArrayList;

public class model_Account  {

    private float balance;
    private String type;
    private int customerId;
    private int accountNumber;



    public model_Account(
        float balance,        String type,        int customerId,        int accountNumber    ) {
        this.balance = balance;
        this.type = type;
        this.customerId = customerId;
        this.accountNumber = accountNumber;
    }


    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getCustomerid() {
        return customerId;
    }

    public void setCustomerid(int customerId) {
        this.customerId = customerId;
    }
    public int getAccountnumber() {
        return accountNumber;
    }

    public void setAccountnumber(int accountNumber) {
        this.accountNumber = accountNumber;
    }


}