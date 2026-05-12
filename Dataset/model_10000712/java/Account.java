





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String pin;
    private String userID;
    private String accountNum;
    private float balance;
    private None type;



    public Account(
        String pin,        String userID,        String accountNum,        float balance,        None type    ) {
        this.pin = pin;
        this.userID = userID;
        this.accountNum = accountNum;
        this.balance = balance;
        this.type = type;
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
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }


}