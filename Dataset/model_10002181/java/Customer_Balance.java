





import java.util.List;
import java.util.ArrayList;

public class Customer_Balance  {

    private String Date;
    private int CustomerID;
    private String Account_balance;
    private String CustomerName;
    private String Adress;



    public Customer_Balance(
        String Date,        int CustomerID,        String Account_balance,        String CustomerName,        String Adress    ) {
        this.Date = Date;
        this.CustomerID = CustomerID;
        this.Account_balance = Account_balance;
        this.CustomerName = CustomerName;
        this.Adress = Adress;
    }


    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public int getCustomerid() {
        return CustomerID;
    }

    public void setCustomerid(int CustomerID) {
        this.CustomerID = CustomerID;
    }
    public String getAccount_balance() {
        return Account_balance;
    }

    public void setAccount_balance(String Account_balance) {
        this.Account_balance = Account_balance;
    }
    public String getCustomername() {
        return CustomerName;
    }

    public void setCustomername(String CustomerName) {
        this.CustomerName = CustomerName;
    }
    public String getAdress() {
        return Adress;
    }

    public void setAdress(String Adress) {
        this.Adress = Adress;
    }


}