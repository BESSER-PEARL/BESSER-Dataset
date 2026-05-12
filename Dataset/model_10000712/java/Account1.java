





import java.util.List;
import java.util.ArrayList;

public class Account1  {

    private float balance;
    private None type;
    private String accountNum;
    private String pin;
    private String userID;



    public Account1(
        float balance,        None type,        String accountNum,        String pin,        String userID    ) {
        this.balance = balance;
        this.type = type;
        this.accountNum = accountNum;
        this.pin = pin;
        this.userID = userID;
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
    public String getAccountnum() {
        return accountNum;
    }

    public void setAccountnum(String accountNum) {
        this.accountNum = accountNum;
    }
    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
    }
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }


}