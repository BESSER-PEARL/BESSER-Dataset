





import java.util.List;
import java.util.ArrayList;

public class Account2  {

    private String userID;
    private String pin;
    private String accountNum;
    private None type;
    private float balance;



    public Account2(
        String userID,        String pin,        String accountNum,        None type,        float balance    ) {
        this.userID = userID;
        this.pin = pin;
        this.accountNum = accountNum;
        this.type = type;
        this.balance = balance;
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


}