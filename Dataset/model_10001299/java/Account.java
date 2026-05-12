





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String MAX_HOLDERS;
    private String accId;
    private String openDate;
    private String accNumber;
    private String balance;



    public Account(
        String MAX_HOLDERS,        String accId,        String openDate,        String accNumber,        String balance    ) {
        this.MAX_HOLDERS = MAX_HOLDERS;
        this.accId = accId;
        this.openDate = openDate;
        this.accNumber = accNumber;
        this.balance = balance;
    }


    public String getMax_holders() {
        return MAX_HOLDERS;
    }

    public void setMax_holders(String MAX_HOLDERS) {
        this.MAX_HOLDERS = MAX_HOLDERS;
    }
    public String getAccid() {
        return accId;
    }

    public void setAccid(String accId) {
        this.accId = accId;
    }
    public String getOpendate() {
        return openDate;
    }

    public void setOpendate(String openDate) {
        this.openDate = openDate;
    }
    public String getAccnumber() {
        return accNumber;
    }

    public void setAccnumber(String accNumber) {
        this.accNumber = accNumber;
    }
    public String getBalance() {
        return balance;
    }

    public void setBalance(String balance) {
        this.balance = balance;
    }


}