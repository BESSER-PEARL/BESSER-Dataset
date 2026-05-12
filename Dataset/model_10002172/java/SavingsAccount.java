





import java.util.List;
import java.util.ArrayList;

public class SavingsAccount  {

    private String Cust_Name;
    private int CustomerId;
    private String Diposit;
    private String Cust_DOB;
    private String Amount;
    private int AccountNo;
    private String AccountType;
    private int Mobile;
    private String Withdraw;





    private Customer customer;


    public SavingsAccount(
        String Cust_Name,        int CustomerId,        String Diposit,        String Cust_DOB,        String Amount,        int AccountNo,        String AccountType,        int Mobile,        String Withdraw    ) {
        this.Cust_Name = Cust_Name;
        this.CustomerId = CustomerId;
        this.Diposit = Diposit;
        this.Cust_DOB = Cust_DOB;
        this.Amount = Amount;
        this.AccountNo = AccountNo;
        this.AccountType = AccountType;
        this.Mobile = Mobile;
        this.Withdraw = Withdraw;
    }


    public String getCust_name() {
        return Cust_Name;
    }

    public void setCust_name(String Cust_Name) {
        this.Cust_Name = Cust_Name;
    }
    public int getCustomerid() {
        return CustomerId;
    }

    public void setCustomerid(int CustomerId) {
        this.CustomerId = CustomerId;
    }
    public String getDiposit() {
        return Diposit;
    }

    public void setDiposit(String Diposit) {
        this.Diposit = Diposit;
    }
    public String getCust_dob() {
        return Cust_DOB;
    }

    public void setCust_dob(String Cust_DOB) {
        this.Cust_DOB = Cust_DOB;
    }
    public String getAmount() {
        return Amount;
    }

    public void setAmount(String Amount) {
        this.Amount = Amount;
    }
    public int getAccountno() {
        return AccountNo;
    }

    public void setAccountno(int AccountNo) {
        this.AccountNo = AccountNo;
    }
    public String getAccounttype() {
        return AccountType;
    }

    public void setAccounttype(String AccountType) {
        this.AccountType = AccountType;
    }
    public int getMobile() {
        return Mobile;
    }

    public void setMobile(int Mobile) {
        this.Mobile = Mobile;
    }
    public String getWithdraw() {
        return Withdraw;
    }

    public void setWithdraw(String Withdraw) {
        this.Withdraw = Withdraw;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}