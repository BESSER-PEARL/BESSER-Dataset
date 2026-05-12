





import java.util.List;
import java.util.ArrayList;

public class account_Account  {

    private float balance;
    private None type;
    private String userID;
    private String pin;
    private String accountNum;



    public account_Account(
        float balance,        None type,        String userID,        String pin,        String accountNum    ) {
        this.balance = balance;
        this.type = type;
        this.userID = userID;
        this.pin = pin;
        this.accountNum = accountNum;
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
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
    }
    public String getAccountnum() {
        return accountNum;
    }

    public void setAccountnum(String accountNum) {
        this.accountNum = accountNum;
    }


}