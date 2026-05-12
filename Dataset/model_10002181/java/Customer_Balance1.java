





import java.util.List;
import java.util.ArrayList;

public class Customer_Balance1  {

    private String CustomerName;
    private String Date;
    private int CustomerID;
    private String Account_balance;
    private String Adress;





    private Customer1 customer1;


    public Customer_Balance1(
        String CustomerName,        String Date,        int CustomerID,        String Account_balance,        String Adress    ) {
        this.CustomerName = CustomerName;
        this.Date = Date;
        this.CustomerID = CustomerID;
        this.Account_balance = Account_balance;
        this.Adress = Adress;
    }


    public String getCustomername() {
        return CustomerName;
    }

    public void setCustomername(String CustomerName) {
        this.CustomerName = CustomerName;
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
    public String getAdress() {
        return Adress;
    }

    public void setAdress(String Adress) {
        this.Adress = Adress;
    }

    public Customer1 getCustomer1() {
        return customer1;
    }

    public void setCustomer1(Customer1 customer1) {
        this.customer1 = customer1;
    }

}