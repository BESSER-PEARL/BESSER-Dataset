





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private None accountType;
    private int PIN;
    private int accountNo;
    private String openedDate;
    private String availableBalance;



    public Account(
        None accountType,        int PIN,        int accountNo,        String openedDate,        String availableBalance    ) {
        this.accountType = accountType;
        this.PIN = PIN;
        this.accountNo = accountNo;
        this.openedDate = openedDate;
        this.availableBalance = availableBalance;
    }


    public None getAccounttype() {
        return accountType;
    }

    public void setAccounttype(None accountType) {
        this.accountType = accountType;
    }
    public int getPin() {
        return PIN;
    }

    public void setPin(int PIN) {
        this.PIN = PIN;
    }
    public int getAccountno() {
        return accountNo;
    }

    public void setAccountno(int accountNo) {
        this.accountNo = accountNo;
    }
    public String getOpeneddate() {
        return openedDate;
    }

    public void setOpeneddate(String openedDate) {
        this.openedDate = openedDate;
    }
    public String getAvailablebalance() {
        return availableBalance;
    }

    public void setAvailablebalance(String availableBalance) {
        this.availableBalance = availableBalance;
    }


}