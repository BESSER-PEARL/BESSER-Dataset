





import java.util.List;
import java.util.ArrayList;

public class account_Account  {

    private String pin;
    private None type;
    private String userID;
    private String accountNum;
    private float balance;



    public account_Account(
        String pin,        None type,        String userID,        String accountNum,        float balance    ) {
        this.pin = pin;
        this.type = type;
        this.userID = userID;
        this.accountNum = accountNum;
        this.balance = balance;
    }


    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public String getAccountnum() {
        return accountNum;
    }

    public void setAccountnum(String accountNum) {
        this.accountNum = accountNum;
    }
    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }


}