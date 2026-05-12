





import java.util.List;
import java.util.ArrayList;

public class CheckingAccount  {

    private String Diposit;
    private int CustomerId;
    private String Withdraw;
    private String Cust_Name;
    private String AccountType;
    private String Cust_DOB;
    private int MobileNo;
    private String Amount;
    private int AccountNo;





    private Customer customer;


    public CheckingAccount(
        String Diposit,        int CustomerId,        String Withdraw,        String Cust_Name,        String AccountType,        String Cust_DOB,        int MobileNo,        String Amount,        int AccountNo    ) {
        this.Diposit = Diposit;
        this.CustomerId = CustomerId;
        this.Withdraw = Withdraw;
        this.Cust_Name = Cust_Name;
        this.AccountType = AccountType;
        this.Cust_DOB = Cust_DOB;
        this.MobileNo = MobileNo;
        this.Amount = Amount;
        this.AccountNo = AccountNo;
    }


    public String getDiposit() {
        return Diposit;
    }

    public void setDiposit(String Diposit) {
        this.Diposit = Diposit;
    }
    public int getCustomerid() {
        return CustomerId;
    }

    public void setCustomerid(int CustomerId) {
        this.CustomerId = CustomerId;
    }
    public String getWithdraw() {
        return Withdraw;
    }

    public void setWithdraw(String Withdraw) {
        this.Withdraw = Withdraw;
    }
    public String getCust_name() {
        return Cust_Name;
    }

    public void setCust_name(String Cust_Name) {
        this.Cust_Name = Cust_Name;
    }
    public String getAccounttype() {
        return AccountType;
    }

    public void setAccounttype(String AccountType) {
        this.AccountType = AccountType;
    }
    public String getCust_dob() {
        return Cust_DOB;
    }

    public void setCust_dob(String Cust_DOB) {
        this.Cust_DOB = Cust_DOB;
    }
    public int getMobileno() {
        return MobileNo;
    }

    public void setMobileno(int MobileNo) {
        this.MobileNo = MobileNo;
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

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}