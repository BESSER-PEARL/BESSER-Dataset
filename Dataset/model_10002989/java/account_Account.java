





import java.util.List;
import java.util.ArrayList;

public class account_Account  {

    private String accountNo;
    private float balance;
    private None type;



    public account_Account(
        String accountNo,        float balance,        None type    ) {
        this.accountNo = accountNo;
        this.balance = balance;
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
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }


}