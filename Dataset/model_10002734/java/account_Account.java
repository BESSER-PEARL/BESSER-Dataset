





import java.util.List;
import java.util.ArrayList;

public class account_Account  {

    private None type;
    private String accountNo;
    private float balance;





    private Customer customer;


    public account_Account(
        None type,        String accountNo,        float balance    ) {
        this.type = type;
        this.accountNo = accountNo;
        this.balance = balance;
    }


    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getAccountno() {
        return accountNo;
    }

    public void setAccountno(String accountNo) {
        this.accountNo = accountNo;
    }
    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}