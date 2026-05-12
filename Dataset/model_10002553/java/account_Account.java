





import java.util.List;
import java.util.ArrayList;

public class account_Account  {

    private None type;
    private float balance;
    private String accountNo;



    public account_Account(
        None type,        float balance,        String accountNo    ) {
        this.type = type;
        this.balance = balance;
        this.accountNo = accountNo;
    }


    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }
    public String getAccountno() {
        return accountNo;
    }

    public void setAccountno(String accountNo) {
        this.accountNo = accountNo;
    }


}